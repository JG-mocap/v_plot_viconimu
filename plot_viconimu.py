from __future__ import print_function
import ViconNexus
from plotly import tools
import plotly.offline as offline
import plotly.graph_objs as go
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

        # plot
        fig = tools.make_subplots(rows=5, cols=3, print_grid=False)

        trace1accel_IMU = go.Scatter(
            y=eccel_x,
            mode='lines',
            name='accelX',
            line=dict(
                color= color_accel,
                width=1)
        )
        trace2accel_IMU = go.Scatter(
            y=eccel_y,
            mode='lines',
            name='accelY',
            line=dict(
                color=color_accel,
                width=1)
        )
        trace3accel_IMU = go.Scatter(
            y=eccel_z,
            mode='lines',
            name='accelZ',
            line=dict(
                color=color_accel,
                width=1)
        )
        trace4gyro_IMU = go.Scatter(
            y=gyro_x,
            mode='lines',
            name='gyroX',
            line=dict(
                color=color_gyro,
                width=1)
        )
        trace5gyro_IMU = go.Scatter(
            y=gyro_y,
            mode='lines',
            name='gyroY',
            line=dict(
                color=color_gyro,
                width=1)
        )
        trace6gyro_IMU = go.Scatter(
            y=gyro_z,
            mode='lines',
            name='gyroZ',
            line=dict(
                color=color_gyro,
                width=1)
        )
        trace7mag_IMU = go.Scatter(
            y=mag_x,
            mode='lines',
            name='magX',
            line=dict(
                color=color_mag,
                width=1)
        )
        trace8mag_IMU = go.Scatter(
            y=mag_y,
            mode='lines',
            name='magY',
            line=dict(
                color= color_mag,
                width=1)
        )
        trace9mag_IMU = go.Scatter(
            y=mag_z,
            mode='lines',
            name='magZ',
            line=dict(
                color=color_mag,
                width=1)
        )
        trace10gla_IMU = go.Scatter(
            y=gla_x,
            mode='lines',
            name='glaX',
            line=dict(
                color=color_global,
                width=1)
        )
        trace11gla_IMU = go.Scatter(
            y=gla_y,
            mode='lines',
            name='glaY',
            line=dict(
                color=color_global,
                width=1)
        )
        trace12gla_IMU = go.Scatter(
            y=gla_z,
            mode='lines',
            name='glaZ', 
            line=dict(
                color=color_global,
                width=1)
        )
        
        trace13hig_IMU = go.Scatter(
            y=hig_x,
            mode='lines',
            name='higX',
            line=dict(
                color=color_highG,
                width=1)
        )
        trace14hig_IMU = go.Scatter(
            y=hig_y,
            mode='lines',
            name='higY',
            line=dict(
                color=color_highG,
                width=1)
        )
        trace15hig_IMU = go.Scatter(
            y=hig_z,
            mode='lines',
            name='higZ', 
            line=dict(
                color=color_highG,
                width=1)
        )

        fig.append_trace(trace1accel_IMU, 1, 1)
        fig.append_trace(trace2accel_IMU, 1, 2)
        fig.append_trace(trace3accel_IMU, 1, 3)

        fig.append_trace(trace4gyro_IMU, 2, 1)
        fig.append_trace(trace5gyro_IMU, 2, 2)
        fig.append_trace(trace6gyro_IMU, 2, 3)

        fig.append_trace(trace7mag_IMU, 3, 1)
        fig.append_trace(trace8mag_IMU, 3, 2)
        fig.append_trace(trace9mag_IMU, 3, 3)
        
        fig.append_trace(trace10gla_IMU, 4, 1)
        fig.append_trace(trace11gla_IMU, 4, 2)
        fig.append_trace(trace12gla_IMU, 4, 3)
        
        fig.append_trace(trace13hig_IMU, 5, 1)
        fig.append_trace(trace14hig_IMU, 5, 2)
        fig.append_trace(trace15hig_IMU, 5, 3)


        filename = dname + ' IMU.html'

        IMU_TrialName = SessionLoc + vicon.GetTrialName()[1] +' ' + filename

        fig['layout'].update(height=2000, width=1800, title=dname + ' IMU Data', plot_bgcolor='#adb5bd')

        offline.plot(fig, filename=IMU_TrialName)

    else:
        print('IMU device not found')

print("Graphs Generated - Time Elapsed: {0:.4f} sec".format(time.clock() - start_time))