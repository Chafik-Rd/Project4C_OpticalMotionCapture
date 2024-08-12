import sys
import os
import time
import copy

from PySide6 import QtWidgets, QtGui, QtCore
from ui import Ui_MainWindow
# from pyqtgraph.ptime import time
from pyqtgraph.widgets.RawImageWidget import RawImageWidget
import pyqtgraph as pg

import pickle
import json
import numpy as np
import cv2
import matplotlib.pyplot as plt

import DLT
import Detect_color

#KT
# COLOR_PRESET = {
# "Green" : Detect_color.COLOR("green",side_lower=[46,83,68], 
#                 side_upper=[59,139,255], 
#                 top_lower=[42,67,33], 
#                 top_upper=[53,144,255], 
#                 draw_color=[255,0,0]),

# "Pink" : Detect_color.COLOR("pink",side_lower=[159,87,74], 
#             side_upper=[169,206,255], 
#             top_lower=[160,108,60], 
#             top_upper=[175,214,255], 
#             draw_color=[0,255,0]),

# "Yellow" : Detect_color.COLOR("yellow",side_lower=[23,90,169], 
#             side_upper=[34,126,255], 
#             top_lower=[29,80,167], 
#             top_upper=[37,123,255], 
#             draw_color=[0,0,255])
# }
# KT  Mahidol Blue
# COLOR_PRESET = {
# "Green" : Detect_color.COLOR("green",side_lower=[46,83,68], 
#                 side_upper=[59,139,255], 
#                 top_lower=[70,88,93], 
#                 top_upper=[76,159,255], 
#                 draw_color=[255,0,0]),

# "Pink" : Detect_color.COLOR("pink",side_lower=[159,87,74], 
#             side_upper=[169,206,255], 
#             top_lower=[143,107,22], 
#             top_upper=[156,193,255], 
#             draw_color=[0,255,0]),

# "Yellow" : Detect_color.COLOR("yellow",side_lower=[23,90,169], 
#             side_upper=[34,126,255], 
#             top_lower=[53,45,193], 
#             top_upper=[65,98,255], 
#             draw_color=[0,0,255])
# }

COLOR_PRESET = {
"Green" : Detect_color.COLOR("green",side_lower=[38,144,62], 
                side_upper=[47,201,255], 
                top_lower=[46,55,42], 
                top_upper=[59,129,255], 
                draw_color=[255,0,0]),

"Pink" : Detect_color.COLOR("pink",side_lower=[163,158,84], 
            side_upper=[179,229,255], 
            top_lower=[156,111,33], 
            top_upper=[169,193,255], 
            draw_color=[0,255,0]),

"Yellow" : Detect_color.COLOR("yellow",side_lower=[24,136,148], 
            side_upper=[29,200,255], 
            top_lower=[36,91,102], 
            top_upper=[39,124,255], 
            draw_color=[0,0,255])
}

class Motion(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.img_fname_save = 0
        self.images = []
        self.xyz = []
        self.all_color = []
        self.proj_mat_l, self.proj_mat_r = None, None
        self.L_mean, self.R_mean = None, None
        
        # config frame setting
        self.calibrat_side_frame.setAspectLocked()
        self.calibrat_top_frame.setAspectLocked()
        self.cali_result_frame.setAspectLocked()
        self.detect_side_frame.setAspectLocked()
        self.detect_top_frame.setAspectLocked()
        
        # slider setting
        self.calibrat_sli_frame.sliderReleased.connect(self.calibrat_slider)
        self.calibrat_result_sli_frame.valueChanged.connect(self.slider_result_show)
        
        self.color_hue_min_side.valueChanged.connect(self.color_side_show_HSV)
        self.color_sat_min_side.valueChanged.connect(self.color_side_show_HSV)
        self.color_value_min_side.valueChanged.connect(self.color_side_show_HSV)
        self.color_hue_max_side.valueChanged.connect(self.color_side_show_HSV)
        self.color_sat_max_side.valueChanged.connect(self.color_side_show_HSV)
        self.color_value_max_side.valueChanged.connect(self.color_side_show_HSV)
        
        self.color_hue_min_top.valueChanged.connect(self.color_top_show_HSV)
        self.color_sat_min_top.valueChanged.connect(self.color_top_show_HSV)
        self.color_value_min_top.valueChanged.connect(self.color_top_show_HSV)
        self.color_hue_max_top.valueChanged.connect(self.color_top_show_HSV)
        self.color_sat_max_top.valueChanged.connect(self.color_top_show_HSV)
        self.color_value_max_top.valueChanged.connect(self.color_top_show_HSV)
        
        self.detect_sli_frame.valueChanged.connect(self.detect_slider)
        
        # Image frame setting
        self.side_img = pg.ImageItem() # create example image
        self.calibrat_side_frame.addItem(self.side_img)
        
        self.top_img = pg.ImageItem() # create example image
        self.calibrat_top_frame.addItem(self.top_img)
        
        self.cali_result_img = pg.ImageItem() # create example image
        self.cali_result_frame.addItem(self.cali_result_img)
        
        self.side_img_detect = pg.ImageItem() # create example image
        self.detect_side_frame.addItem(self.side_img_detect)
        
        self.top_img_detect = pg.ImageItem() # create example image
        self.detect_top_frame.addItem(self.top_img_detect)
        
        # Disable Axis
        self.calibrat_side_frame.showAxes(False)
        self.calibrat_top_frame.showAxes(False)
        self.cali_result_frame.showAxes(False)
        self.detect_side_frame.showAxes(False)
        self.detect_top_frame.showAxes(False)
        
        # Disable Button
        self.calibrat_btn_undo.setDisabled(True)
        self.calibrat_btn_reset.setDisabled(True)
        self.calibrat_btn_cali.setDisabled(True)
        self.calibrat_btn_save.setDisabled(True)
        self.detect_btn_run.setDisabled(True)
        self.detect_btn_savevideo.setDisabled(True)
        
        # Get values
        self.toolButton_LV1.clicked.connect(self.browse_file_LV1)
        self.toolButton_LV2.clicked.connect(self.browse_file_LV2)
        self.btn_load.clicked.connect(self.load_video)
        
        self.calibrat_btn_store.clicked.connect(self.calibrat_store)
        self.calibrat_btn_undo.clicked.connect(self.calibrat_undo)
        self.calibrat_btn_reset.clicked.connect(self.calibrat_reset)
        self.calibrat_btn_cali.clicked.connect(self.calibrat)
        self.calibrat_btn_save.clicked.connect(self.calibrat_save)
        
        self.color_btn_save.clicked.connect(self.color_save)
        self.color_btn_undo.clicked.connect(self.color_undo)
        
        self.detect_btn_start.clicked.connect(self.detect_start)
        self.detect_btn_stop.clicked.connect(self.detect_stop)
        self.detect_btn_run.clicked.connect(self.detect)
        self.detect_toolButton_filepoint.clicked.connect(self.detect_browse_file_Point)
        self.detect_toolButton_filecalibrat.clicked.connect(self.detect_browse_file_Calibrat)
        self.detect_btn_plot.clicked.connect(self.detect_plot)
        
        # Color Preset
        self.color_comboBox.currentTextChanged.connect(self.color_preset)

    def browse_file_LV1(self):
        self.fname_side = str(QtWidgets.QFileDialog.getOpenFileName(caption="Open Side Video", filter="Videos (*.mov *.mp4 *.avi)")[0])
        self.lineEdit_LV1.setText(self.fname_side)
        
    def browse_file_LV2(self):
        self.fname_top = str(QtWidgets.QFileDialog.getOpenFileName(caption="Open Top Video", filter="Videos (*.mov *.mp4 *.avi)")[0])
        self.lineEdit_LV2.setText(self.fname_top)
    
    def load_video(self):
        if self.checkBox_sync.isChecked():
            pass

        self.cap_side = cv2.VideoCapture(self.fname_side)
        self.cap_top = cv2.VideoCapture(self.fname_top)
    
        frame_count = min(int(self.cap_side.get(cv2.CAP_PROP_FRAME_COUNT)), int(self.cap_top.get(cv2.CAP_PROP_FRAME_COUNT)))
        
        self.calibrat_sli_frame.setMaximum(frame_count-1)
        self.detect_sli_frame.setMaximum(frame_count-1)
        self.detect_spinBox_start.setMaximum(frame_count-1)
        self.detect_spinBox_stop.setMaximum(frame_count-1)
    
    def calibrat_slider(self):
        print(self.calibrat_sli_frame.value())
        self.cap_side.set(cv2.CAP_PROP_POS_FRAMES, self.calibrat_sli_frame.value())
        self.cap_top.set(cv2.CAP_PROP_POS_FRAMES, self.calibrat_sli_frame.value())
        
        ret_side, self.img_side = self.cap_side.read()
        ret_top, self.img_top = self.cap_top.read()
        if ret_side and ret_top:
            dst_side = cv2.rotate(self.img_side, cv2.ROTATE_90_CLOCKWISE)
            self.side_img.setImage(cv2.cvtColor(dst_side,cv2.COLOR_BGR2RGB))
            
            dst_top = cv2.rotate(self.img_top, cv2.ROTATE_90_CLOCKWISE)
            self.top_img.setImage(cv2.cvtColor(dst_top,cv2.COLOR_BGR2RGB))
            
    def calibrat_store(self):
        cv2.imwrite("C:/Users/fikky/Desktop/s/" + str(self.img_fname_save) + ".png", self.img_side)
        cv2.imwrite("C:/Users/fikky/Desktop/t/" + str(self.img_fname_save) + ".png", self.img_top)
        self.images.append((self.img_side, self.img_top))
        self.xyz.append((int(self.calibrat_spinBox_x.value()), int(self.calibrat_spinBox_y.value()), int(self.calibrat_spinBox_z.value())))
        print(self.xyz)
        self.img_fname_save += 1
        

        self.calibrat_btn_undo.setEnabled(True)
        self.calibrat_btn_reset.setEnabled(True)
        self.calibrat_btn_cali.setEnabled(True)
        self.calibrat_btn_save.setEnabled(True)

    def calibrat_undo(self):
        self.images.pop()
        self.xyz.pop()
        print(self.xyz)
        
    def calibrat_reset(self):
        self.images.clear()
        self.xyz.clear()
        print(self.xyz)
        
    def calibrat(self):
        W = int(self.calibrat_spinBox_Wboard.value())
        H = int(self.calibrat_spinBox_Hboard.value())
            
        if self.calibrat_checkBox_opencv.isChecked():
            
            chessboardSize = (W,H)

            # Termination criteria for refining the detected corners
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)


            objp = np.zeros((chessboardSize[0] * chessboardSize[1],3), np.float32)
            objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)

            size_of_chessboard_squares_mm = self.calibrat_spinBox_sizesq.value()
            objp = objp * size_of_chessboard_squares_mm
            
            img_ptsL = []
            img_ptsR = []
            obj_pts = []
            
            for i in range(len(self.xyz)):
                img_side = self.images[i][0]
                img_top = self.images[i][1]

                imgL_gray = cv2.cvtColor(img_side, cv2.COLOR_BGR2GRAY)
                imgR_gray = cv2.cvtColor(img_top, cv2.COLOR_BGR2GRAY)
                outputL = img_side.copy()
                outputR = img_top.copy()

                retR, cornersR =  cv2.findChessboardCorners(outputR,chessboardSize,None)
                retL, cornersL = cv2.findChessboardCorners(outputL,chessboardSize,None)

                if retR and retL:
                    obj_pts.append(objp)
                    cv2.cornerSubPix(imgR_gray, cornersR, (11,11), (-1,-1), criteria)
                    cv2.cornerSubPix(imgL_gray, cornersL, (11,11), (-1,-1), criteria)
                    img_ptsR.append(cornersR)
                    img_ptsL.append(cornersL)


            # Calibrating left camera
            retL, mtxL, distL, rvecsL, tvecsL = cv2.calibrateCamera(obj_pts,img_ptsL,imgL_gray.shape[::-1],None,None)
            hL,wL= imgL_gray.shape[:2]
            new_mtxL, roiL= cv2.getOptimalNewCameraMatrix(mtxL,distL,(wL,hL),1,(wL,hL))

            # Calibrating right camera
            retR, mtxR, distR, rvecsR, tvecsR = cv2.calibrateCamera(obj_pts,img_ptsR,imgR_gray.shape[::-1],None,None)
            hR,wR= imgR_gray.shape[:2]
            new_mtxR, roiR= cv2.getOptimalNewCameraMatrix(mtxR,distR,(wR,hR),1,(wR,hR))
            
            flags = 0
            flags |= cv2.CALIB_FIX_INTRINSIC
            # Here we fix the intrinsic camara matrixes so that only Rot, Trns, Emat and Fmat are calculated.
            # Hence intrinsic parameters are the same

            # This step is performed to transformation between the two cameras and calculate Essential and Fundamenatl matrix
            retS, new_mtxL, distL, new_mtxR, distR, Rot, Trns, Emat, Fmat = cv2.stereoCalibrate(obj_pts, 
                                                                                                img_ptsL, 
                                                                                                img_ptsR, 
                                                                                                new_mtxL, 
                                                                                                distL, 
                                                                                                new_mtxR, 
                                                                                                distR, 
                                                                                                imgL_gray.shape[::-1], 
                                                                                                criteria, 
                                                                                                flags
                                                                                                )
            RT1 = np.concatenate([np.eye(3), [[0],[0],[0]]], axis = -1)
            self.P1 = new_mtxL @ RT1

            RT2 = np.concatenate([Rot, Trns], axis = -1)
            self.P2 = new_mtxR @ RT2

            rectify_scale = 1
            rect_l, rect_r, self.proj_mat_l, self.proj_mat_r, Q, roiL, roiR= cv2.stereoRectify(new_mtxL, 
                                                                                     distL, 
                                                                                     new_mtxR, 
                                                                                     distR, 
                                                                                     imgL_gray.shape[::-1], 
                                                                                     Rot, 
                                                                                     Trns, 
                                                                                     rectify_scale,
                                                                                     (0,0)
                                                                                     )
            
            with open("opcv_proj_mtrx.param","wb") as file:
                pickle.dump((self.P1, self.P2),file)
            # for i in range(len(self.xyz)):
            #     img_side = self.images[i][0]
            #     img_top = self.images[i][1]
                
            

        else:
            L_total = np.zeros((11,))
            R_total = np.zeros((11,))
            
            dg = int(self.calibrat_spinBox_drgree.value())
            sqSize = int(self.calibrat_spinBox_sizesq.value())
            
            self.cali_result_images_list = []
            for i in range(len(self.xyz)):
                img_side = self.images[i][0]
                img_top = self.images[i][1]
                
                self.dlt = DLT.DLT(self.images[i][0],
                            self.images[i][1],
                            W,
                            H,
                            dg,
                            sqSize,
                            self.xyz[i])
                L, R = self.dlt.LR_minimum_err(20,20,2000)
                L_total += L
                R_total += R
                
                uL, vL, uR, vR = self.dlt.get_uv()
                
                img_side = cv2.drawChessboardCorners(img_side, (W, H), self.dlt.corners1original, True)
                img_top = cv2.drawChessboardCorners(img_top, (W, H), self.dlt.corners2original, True)
                
                for j in range(len(uL)):
                    cv2.circle(img_side, (uL[j], vL[j]), 0, (225,0,0), 3)
                    cv2.circle(img_top, (uR[j], vR[j]), 0, (225,0,0), 3)
                
                img_side = cv2.rotate(img_side, cv2.ROTATE_90_CLOCKWISE)
                img_top = cv2.rotate(img_top, cv2.ROTATE_90_CLOCKWISE)
                
                self.cali_result_images_list.append(cv2.cvtColor(np.vstack([img_side, img_top]), cv2.COLOR_BGR2RGB))
            
            self.cali_result_img.setImage(self.cali_result_images_list[0])
            self.calibrat_result_sli_frame.setMaximum(len(self.cali_result_images_list)-1)
            self.L_mean = L_total/len(self.xyz)
            self.R_mean = R_total/len(self.xyz)
        
    def calibrat_save(self):
        with open("mean_LR.param","wb") as file:
            pickle.dump((self.L_mean, self.R_mean),file)
        
    def slider_result_show(self):
        self.cali_result_img.setImage(self.cali_result_images_list[self.calibrat_result_sli_frame.value()])
        
    def color_preset(self):
        self.color_hue_min_side.setValue(COLOR_PRESET[self.color_comboBox.currentText()]["side"]["range"]["lower"][0]),
        self.color_sat_min_side.setValue(COLOR_PRESET[self.color_comboBox.currentText()]["side"]["range"]["lower"][1]),
        self.color_value_min_side.setValue(COLOR_PRESET[self.color_comboBox.currentText()]["side"]["range"]["lower"][2]),
        self.color_hue_max_side.setValue(COLOR_PRESET[self.color_comboBox.currentText()]["side"]["range"]["upper"][0]),
        self.color_sat_max_side.setValue(COLOR_PRESET[self.color_comboBox.currentText()]["side"]["range"]["upper"][1]),
        self.color_value_max_side.setValue(COLOR_PRESET[self.color_comboBox.currentText()]["side"]["range"]["upper"][2]),
        self.color_hue_min_top.setValue(COLOR_PRESET[self.color_comboBox.currentText()]["top"]["range"]["lower"][0]),
        self.color_sat_min_top.setValue(COLOR_PRESET[self.color_comboBox.currentText()]["top"]["range"]["lower"][1]),
        self.color_value_min_top.setValue(COLOR_PRESET[self.color_comboBox.currentText()]["top"]["range"]["lower"][2]),
        self.color_hue_max_top.setValue(COLOR_PRESET[self.color_comboBox.currentText()]["top"]["range"]["upper"][0]),
        self.color_sat_max_top.setValue(COLOR_PRESET[self.color_comboBox.currentText()]["top"]["range"]["upper"][1]),
        self.color_value_max_top.setValue(COLOR_PRESET[self.color_comboBox.currentText()]["top"]["range"]["upper"][2]),
    
    def color_save(self):
        self.all_color.append(Detect_color.COLOR(self.color_comboBox.currentText(),
                                                (self.color_hue_min_side.value(),
                                                self.color_sat_min_side.value(),
                                                self.color_value_min_side.value()),
                                                (self.color_hue_max_side.value(),
                                                self.color_sat_max_side.value(),
                                                self.color_value_max_side.value()),
                                                (self.color_hue_min_top.value(),
                                                self.color_sat_min_top.value(),
                                                self.color_value_min_top.value()),
                                                (self.color_hue_max_top.value(),
                                                self.color_sat_max_top.value(),
                                                self.color_value_max_top.value()),
                                                (self.color_hue_min_side.value(),
                                                self.color_sat_min_side.value(),
                                                self.color_value_min_side.value())))
        print(self.all_color)     
    
    def color_undo(self):
        self.all_color.pop()
        print(self.all_color)
    
    def color_side_show_HSV(self):
        lower_side = np.array([self.color_hue_min_side.value(),self.color_sat_min_side.value(),self.color_value_min_side.value()])
        upper_side = np.array([self.color_hue_max_side.value(),self.color_sat_max_side.value(),self.color_value_max_side.value()])
        
        mask_side = cv2.inRange(cv2.cvtColor(self.dst_side_detect ,cv2.COLOR_BGR2HSV), lower_side, upper_side)
        result_side = cv2.bitwise_and(self.dst_side_detect ,self.dst_side_detect, mask = mask_side)
    
        mask_side = cv2.cvtColor(mask_side,cv2.COLOR_GRAY2BGR)
        hStack_side = np.hstack([mask_side,result_side])
        
        self.side_img_detect.setImage(cv2.cvtColor(hStack_side,cv2.COLOR_BGR2RGB))
                
    def color_top_show_HSV(self):
        lower_top = np.array([self.color_hue_min_top.value(),self.color_sat_min_top.value(),self.color_value_min_top.value()])
        upper_top = np.array([self.color_hue_max_top.value(),self.color_sat_max_top.value(),self.color_value_max_top.value()])
        
        mask_top = cv2.inRange(cv2.cvtColor(self.dst_top_detect, cv2.COLOR_BGR2HSV), lower_top, upper_top)
        result_top = cv2.bitwise_and(self.dst_top_detect, self.dst_top_detect, mask = mask_top)
        
        mask_top = cv2.cvtColor(mask_top,cv2.COLOR_GRAY2BGR)
        hStack_top = np.hstack([mask_top,result_top])
        
        self.top_img_detect.setImage(cv2.cvtColor(hStack_top,cv2.COLOR_BGR2RGB))
    
    def detect_slider(self):
        self.cap_side.set(cv2.CAP_PROP_POS_FRAMES, self.detect_sli_frame.value())
        self.cap_top.set(cv2.CAP_PROP_POS_FRAMES, self.detect_sli_frame.value())
        
        ret_side_detect, img_side_detect = self.cap_side.read()
        ret_top_detect, img_top_detect = self.cap_top.read()
        
        if ret_side_detect and ret_top_detect:
            self.dst_side_detect = cv2.rotate(img_side_detect, cv2.ROTATE_90_CLOCKWISE)
            self.dst_top_detect = cv2.rotate(img_top_detect, cv2.ROTATE_90_CLOCKWISE)
            
            if self.detect_toolBox.currentIndex() == 0:
                self.color_side_show_HSV()
                self.color_top_show_HSV()
            else:
                self.side_img_detect.setImage(cv2.cvtColor(self.dst_side_detect,cv2.COLOR_BGR2RGB))
                self.top_img_detect.setImage(cv2.cvtColor(self.dst_top_detect,cv2.COLOR_BGR2RGB))
        
    def detect_start(self):
        self.detect_spinBox_start.setValue(self.detect_sli_frame.value())

    def detect_stop(self):
        self.detect_spinBox_stop.setValue(self.detect_sli_frame.value())

        self.detect_btn_run.setEnabled(True)
        self.detect_btn_savevideo.setEnabled(True)
        
    def detect_save_video(self):
        fourcc = cv2.VideoWriter_fourcc('M','P','4','2')
        out1 = cv2.VideoWriter('Video_Test/18-10-64/combined_P_9.mp4',fourcc, 60.0, (3840,1080))
        out2 = cv2.VideoWriter('Video_Test/18-10-64/topP_7.mp4',fourcc, 60.0, (1280,720))
        dt = Detect_color.Detect(self.fname_side, self.fname_top, self.all_color)
        while True:
            succes, imgs = dt.detect_next_frame()

            if succes:
                img_side, img_top = imgs
            else:
                break
            
            out1.write(img_side)
            out2.write(img_top)
                        
            result = np.hstack([self.img_side,self.img_top])
            # cv2.imshow('Frame',cv2.resize(result,(1280,360)))
                
            out1.write(cv2.resize(result, (3840,1080)))
            
            
            if cv2.waitKey(1) & 0xFF == ord('q') or dt.frame > self.detect_start():
                break
        # Not finish
    
    def update_detect(self):
        success, imgs = self.dt.detect_next_frame()
            
        if success:
            s = cv2.rotate(imgs[0], cv2.ROTATE_90_CLOCKWISE)
            self.side_img_detect.setImage(cv2.cvtColor(s, cv2.COLOR_BGR2RGB))
            t = cv2.rotate(imgs[1], cv2.ROTATE_90_CLOCKWISE)
            self.top_img_detect.setImage(cv2.cvtColor(t, cv2.COLOR_BGR2RGB))
            
        if self.dt.frame > self.detect_spinBox_stop.value() - self.detect_spinBox_start.value():
            self.timer.stop()
            self.marker = self.dt.export_marker_pos()
            with open("OMC.marker", "wb") as file:
                pickle.dump(self.marker, file)    
        
    def get_real_pos(self, J_s, J_t,origin = False):
        if origin:
            origin_pos = self.origin()
        
        if len(J_s) == 1:
            frame_idxL, uvL = [J_s[0][0]], J_s[0][1]
            frame_idxR, uvR = [J_t[0][0]], J_t[0][1]
        else:   
            frame_idxL, uvL = zip(*J_s)
            frame_idxR, uvR = zip(*J_t)
        
        uvL = np.array(uvL, ndmin=2)
        uvR = np.array(uvR, ndmin=2)
        
        real_pos = []
        real_idx = []
        
        if self.detect_checkBox_opencv.isChecked():
            for idx in frame_idxL:
                if idx in frame_idxR:
                    xyz = self.triangulate(self.P1, 
                                           self.P2, 
                                           [uvL[frame_idxL.index(idx)][0], uvL[frame_idxL.index(idx)][1]],
                                           [uvR[frame_idxR.index(idx)][0], uvR[frame_idxR.index(idx)][1]])
                    
                    if origin:
                        real_idx.append([idx])
                        xyz = np.array([xyz[2],xyz[0]*-1,xyz[1]*-1])
                        xyz = np.reshape(xyz-origin_pos, xyz.shape)
                        real_pos.append(xyz)
                        print(idx,xyz)
                    else:
                        real_idx.append([idx])
                        xyz = np.array([xyz[2],xyz[0]*-1,xyz[1]*-1])
                        real_pos.append(xyz)
                        print(idx,xyz)
            return np.array(real_idx), np.array(real_pos)
        
        else:
            if self.L_mean is None or self.R_mean is None:
                raise ValueError("No DLT parameters founded, load or calibrate the videos first")
            for idx in frame_idxL:
                if idx in frame_idxR:
                    xyz = self.dlt.get_XYZ(uvL[frame_idxL.index(idx)][0], uvL[frame_idxL.index(idx)][1], uvR[frame_idxR.index(idx)][0], uvR[frame_idxR.index(idx)][1], useOrigin=False)
                    xyz[2] , xyz[1] = self.dlt.rotate(xyz[2],xyz[1],-60)
                    xyz[0] , xyz[1] = self.dlt.rotate(xyz[0],xyz[1],-30)
                    if origin:
                        real_idx.append([idx])
                        xyz = np.reshape(xyz-origin_pos, xyz.shape)
                        real_pos.append(xyz)
                        print(idx,xyz)
                    else:
                        real_idx.append([idx])
                        real_pos.append(xyz)
                        print(idx,xyz)
                        
                    # real_idx.append([idx])
                    # real_pos.append(xyz)
            return np.array(real_idx), np.array(real_pos)     
     
    def detect(self):
        Detect_color.WIDTH = self.detect_spinBox_setW.value()
        Detect_color.HEIGHT = self.detect_spinBox_setH.value()
        
        self.dt = Detect_color.Detect(self.fname_side, self.fname_top, copy.deepcopy(self.all_color))
        
        self.dt.cap_side.set(cv2.CAP_PROP_POS_FRAMES, self.detect_spinBox_start.value())
        self.dt.cap_top.set(cv2.CAP_PROP_POS_FRAMES, self.detect_spinBox_start.value())
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_detect)
        self.timer.start()
     
    def detect_browse_file_Point(self):
        self.file_point = str(QtWidgets.QFileDialog.getOpenFileName(caption="Open File Point Detect", filter="Videos (*.marker)")[0])
        self.detect_lineEdit_filepoint.setText(self.file_point)           
        
    def detect_browse_file_Calibrat(self):
        self.file_calibrat = str(QtWidgets.QFileDialog.getOpenFileName(caption="Open File Calibration", filter="Videos (*.param)")[0])
        self.detect_lineEdit_filecalibrat.setText(self.file_calibrat) 

    def triangulate(self, P1, P2, point1, point2):
        
        A = [point1[1]*P1[2,:] - P1[1,:],
            P1[0,:] - point1[0]*P1[2,:],
            point2[1]*P2[2,:] - P2[1,:],
            P2[0,:] - point2[0]*P2[2,:]
            ]
        A = np.array(A).reshape((4,4))
        #print('A: ')
        #print(A)
    
        B = A.transpose() @ A
        from scipy import linalg
        U, s, Vh = linalg.svd(B, full_matrices = False)
    
        # print('Triangulated point: ')
        # print(Vh[3,0:3]/Vh[3,3])
        return Vh[3,0:3]/Vh[3,3]
    
    def origin(self):
        origin_idx, origin_pos = self.get_real_pos([self.marker["Green"]["side"][0]], [self.marker["Green"]["top"][0]])
        return origin_pos
    
    def detect_plot(self):
        with open("opcv_proj_mtrx.param","rb") as file:
            self.P1, self.P2 = pickle.load(file)
            
        with open("OMC.marker", "rb") as file:
            self.marker = pickle.load(file) 
        
        
        G_real_idx, G_real_pos = self.get_real_pos(self.marker["Green"]["side"], self.marker["Green"]["top"],origin=True)
        Y_real_idx, Y_real_pos = self.get_real_pos(self.marker["Yellow"]["side"], self.marker["Yellow"]["top"],origin=True)
        P_real_idx, P_real_pos = self.get_real_pos(self.marker["Pink"]["side"], self.marker["Pink"]["top"],origin=True) 
        
       
        # with open("G1.csv", "w") as file:
        #     file.write("X,Y,Z\n")
        #     for i in range(len(G_real_idx)):
        #         file.write(str(G_real_pos[i, 2])+',')
        #         file.write(str(G_real_pos[i, 0]*-1)+',')
        #         file.write(str(G_real_pos[i, 1]*-1))
        #         file.write("\n")
                
        with open("KTDLT.WPOS", "wb") as file:
                pickle.dump([G_real_idx, G_real_pos,Y_real_idx, Y_real_pos,P_real_idx, P_real_pos], file) 
            
        
        if self.detect_checkBox_opencv.isChecked():
            fig = plt.figure()
            ax = fig.add_subplot(projection='3d')
            
            ax.set_box_aspect((np.ptp(Y_real_pos[:, 0]), np.ptp(Y_real_pos[:, 1]), np.ptp(Y_real_pos[:, 2])))
            
            ax.plot(Y_real_pos[:, 0], Y_real_pos[:, 1], Y_real_pos[:, 2], color='y')
            ax.plot(G_real_pos[:, 0], G_real_pos[:, 1], G_real_pos[:, 2], color='g')
            ax.plot(P_real_pos[:, 0], P_real_pos[:, 1], P_real_pos[:, 2], color='r')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')

            fig0 = plt.figure()
            x, y = Detect_color.th_in_dist(G_real_pos, G_real_idx, P_real_pos, P_real_idx)
            ax1 = fig0.add_subplot(311)
            ax1.plot(np.array(x)/60,np.array(y))
            ax1.scatter(np.array(x)/60,np.array(y))
            ax1.set_ylabel('Distance(mm)')

            wrist_index, v = Detect_color.velocity(Y_real_idx, Y_real_pos)
            ax2 = fig0.add_subplot(312)
            ax2.plot(np.array(wrist_index)/60,np.array(v)*60)
            ax2.scatter(np.array(wrist_index)/60,np.array(v)*60)
            ax2.set_ylabel('Velocity(mm/sec)')

            ax3 = fig0.add_subplot(313)
            ax3.plot(Y_real_idx/60, (Y_real_pos[:, 2])+90)
            ax3.scatter(Y_real_idx/60, (Y_real_pos[:, 2])+90)
            # ax3.set_ylim(0,250)
            ax3.set_xlabel('Time(Sec)')
            ax3.set_ylabel('Level(mm)')

            plt.show()
        else:
            
            fig = plt.figure()
            ax = fig.add_subplot(projection='3d')
            ax.plot(Y_real_pos[:, 0], Y_real_pos[:, 1], Y_real_pos[:, 2])
            ax.plot(G_real_pos[:, 0], G_real_pos[:, 1], G_real_pos[:, 2])
            ax.plot(P_real_pos[:, 0], P_real_pos[:, 1], P_real_pos[:, 2])
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            # ax.set_xlim3d( -350, 350)
            # ax.set_ylim3d(-500, 200)
            # ax.set_zlim3d( -100, 600)


            fig0 = plt.figure()
            x, y = Detect_color.th_in_dist(G_real_pos, G_real_idx, P_real_pos, P_real_idx)
            ax1 = fig0.add_subplot(311)
            ax1.plot(np.array(x)/60,np.array(y))
            ax1.scatter(np.array(x)/60,np.array(y))
            ax1.set_ylabel('Distance(mm)')
            # 
            # 

            win, v = Detect_color.velocity(Y_real_idx, Y_real_pos)
            ax2 = fig0.add_subplot(312)
            ax2.plot(np.array(win)/60,np.array(v)*60)
            ax2.scatter(np.array(win)/60,np.array(v)*60)
            ax2.set_ylabel('Velocity(mm/sec)')
            # ax2.set_ylim(0,20)


            ax3 = fig0.add_subplot(313)
            ax3.plot(G_real_idx/60, G_real_pos[:, 2])
            ax3.scatter(G_real_idx/60, G_real_pos[:, 2])
            # ax3.set_ylim(0,250)
            ax3.set_xlabel('Time(Sec)')
            ax3.set_ylabel('Level(mm)')

            plt.show()
                            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Motion()
    window.show()
    app.exec()