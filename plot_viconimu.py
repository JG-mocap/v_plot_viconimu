#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from __future__ import print_function
import os, sys
import ViconNexus
from plotly import tools
import plotly.offline as offline
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

print ('Generating IMU device graphs...')

start_time = time.clock()
vicon = ViconNexus.ViconNexus()
SessionLoc = vicon.GetTrialName()[0]
SubjectName = vicon.GetSubjectNames()
devicenames = vicon.GetDeviceNames()

imudevicename = {}

color_accel = '#065374'
color_gyro = '#b61641'
color_mag = '#20ac9e'
color_global = '#73072f'
color_highG = '#051876'

for imudevicename in devicenames:
    if imudevicename in devicenames:
        imuid = vicon.GetDeviceIDFromName(imudevicename)

        dname, dtype, drate, outputids, _, _ = vicon.GetDeviceDetails(imuid)

        # read accel
        outputid = outputids[0]
        accel_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'x')
        eccel_x, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, accel_IMU)
        accel_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'y')
        eccel_y, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, accel_IMU)
        accel_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'z')
        eccel_z, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, accel_IMU)

        # read gyro
        outputid = outputids[1]
        gyro_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'x')
        gyro_x, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, gyro_IMU)
        gyro_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'y')
        gyro_y, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, gyro_IMU)
        gyro_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'z')
        gyro_z, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, gyro_IMU)

        # read mag
        outputid = outputids[2]
        mag_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'x')
        mag_x, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, mag_IMU)
        mag_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'y')
        mag_y, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, mag_IMU)
        mag_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'z')
        mag_z, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, mag_IMU)
        
        # read global ng
        outputid = outputids[3]
        gla_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'x')
        gla_x, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, gla_IMU)
        gla_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'y')
        gla_y, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, gla_IMU)
        gla_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'z')
        gla_z, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, gla_IMU)

        # read high g
        outputid = outputids[4]
        hig_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'x')
        hig_x, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, hig_IMU)
        hig_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'y')
        hig_y, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, hig_IMU)
        hig_IMU = vicon.GetDeviceChannelIDFromName(imuid, outputid, 'z')
        hig_z, chready, chrate = vicon.GetDeviceChannel(imuid, outputid, hig_IMU)

        # create plot area
        fig = make_subplots(rows=5, cols=3, print_grid=False)
        
        # add traces
        fig.add_trace(go.Scatter(y=eccel_x, name = "Acceleration X", line=dict(
            color= color_accel,width=1)),  row=1, col=1)
        fig.update_xaxes(title_text="Frame nr", row=1, col=1)
        fig.update_yaxes(title_text="Accel.x (mm/s<sup>2</sup>)", row=1, col=1)
        
        fig.add_trace(go.Scatter(y=eccel_y, name = "Acceleration Y", line=dict(
            color= color_accel,width=1)), row=1, col=2)
        fig.update_xaxes(title_text="Frame nr", row=1, col=2)
        fig.update_yaxes(title_text="Accel.y (mm/s<sup>2</sup>)", row=1, col=2)
       
        fig.add_trace(go.Scatter(y=eccel_z, name = "Acceleration Z",line=dict(
            color= color_accel,width=1)), row=1, col=3)
        fig.update_xaxes(title_text="Frame nr", row=1, col=3)
        fig.update_yaxes(title_text="Accel.z (mm/s<sup>2</sup>)", row=1, col=3)

        fig.add_trace(go.Scatter(y=gyro_x, name = "Gyroscope X", line=dict(
            color= color_gyro,width=1)), row=2, col=1)
        fig.update_xaxes(title_text="Frame nr", row=2, col=1)
        fig.update_yaxes(title_text="Gyro.x (deg/s)", row=2, col=1)

        fig.add_trace(go.Scatter(y=gyro_y, name = "Gyroscope Y", line=dict(
            color= color_gyro,width=1)), row=2, col=2)
        fig.update_xaxes(title_text="Frame nr", row=2, col=2)
        fig.update_yaxes(title_text="Gyro.y (deg/s)", row=2, col=2)

        fig.add_trace(go.Scatter(y=gyro_z, name = "Gyroscope Z", line=dict(
            color= color_gyro,width=1)), row=2, col=3)
        fig.update_xaxes(title_text="Frame nr", row=2, col=3)
        fig.update_yaxes(title_text="Gyro.z (deg/s)", row=2, col=3)

        fig.add_trace(go.Scatter(y=mag_x, name = "Magnetometer X", line=dict(
            color= color_mag,width=1)), row=3, col=1)
        fig.update_xaxes(title_text="Frame nr", row=3, col=1)
        fig.update_yaxes(title_text="Mag.x (T)", row=3, col=1)

        fig.add_trace(go.Scatter(y=mag_y, name = "Magnetometer Y", line=dict(
            color= color_mag,width=1)), row=3, col=2)
        fig.update_xaxes(title_text="Frame nr", row=3, col=2)
        fig.update_yaxes(title_text= "Mag. field.y (T)", row=3, col=2)
        
        fig.add_trace(go.Scatter(y=mag_z, name = "Magnetometer Z", line=dict(
            color= color_mag,width=1)), row=3, col=3)
        fig.update_xaxes(title_text="Frame nr", row=3, col=3)
        fig.update_yaxes(title_text="Mag.z (T)", row=3, col=3)
        
        fig.add_trace(go.Scatter(y=gla_x, name = "Global Angle X", line=dict(
            color= color_global,width=1)), row=4, col=1)
        fig.update_xaxes(title_text="Frame nr", row=4, col=1)
        fig.update_yaxes(title_text="Global angle.x (deg)", row=4, col=1)
        
        fig.add_trace(go.Scatter(y=gla_y, name = "Global Angle Y", line=dict(
            color= color_global,width=1)), row=4, col=2)
        fig.update_xaxes(title_text="Frame nr", row=4, col=2)
        fig.update_yaxes(title_text="Global angle.y (deg)", row=4, col=2)
        
        fig.add_trace(go.Scatter(y=gla_z, name = "Global Angle Z", line=dict(
            color= color_global,width=1)), row=4, col=3)
        fig.update_xaxes(title_text="Frame nr", row=4, col=3)
        fig.update_yaxes(title_text="Global angle.z (deg)", row=4, col=3)

        fig.add_trace(go.Scatter(y=hig_x, name = "Global Angle X", line=dict(
            color= color_highG,width=1)), row=5, col=1)
        fig.update_xaxes(title_text="Frame nr", row=5, col=1)
        fig.update_yaxes(title_text="HighG.x (deg)", row=5, col=1)
        
        fig.add_trace(go.Scatter(y=hig_y, name = "Global Angle Y", line=dict(
            color= color_highG,width=1)), row=5, col=2)
        fig.update_xaxes(title_text="Frame nr", row=5, col=2)
        fig.update_yaxes(title_text="HighG.y (deg)", row=5, col=2)
        
        fig.add_trace(go.Scatter(y=hig_z, name = "Global Angle Z", line=dict(
            color= color_highG,width=1)), row=5, col=3)
        fig.update_xaxes(title_text="Frame nr", row=5, col=3)
        fig.update_yaxes(title_text="HighG.z (deg)", row=5, col=3)
        
        fig.update_layout(legend_title_text='IMU Outputs')
        fig.update_layout(font_family="Oswald",
                          font_color="#2f3640")

        filename = dname + ' IMU.html'

        IMU_TrialName = SessionLoc + vicon.GetTrialName()[1] +' ' + filename

        fig['layout'].update(height=1800, width=1600, title=dname + ' IMU Data', plot_bgcolor='#dcdde1')

        offline.plot(fig, filename=IMU_TrialName)

    else:
        print('IMU device not found')

print("Graphs Generated - Time Elapsed: {0:.4f} sec".format(time.clock() - start_time))