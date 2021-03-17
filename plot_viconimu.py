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

        # plot
        fig = tools.make_subplots(rows=3, cols=3, print_grid=False)

        trace1accel_IMU = go.Scatter(
            y=eccel_x,
            mode='lines',
            name='accelX',
            line=dict(
                color='rgb(44, 62, 80)',
                width=1)
        )
        trace2accel_IMU = go.Scatter(
            y=eccel_y,
            mode='lines',
            name='accelY',
            line=dict(
                color='rgb(44, 62, 80)',
                width=1)
        )
        trace3accel_IMU = go.Scatter(
            y=eccel_z,
            mode='lines',
            name='accelZ',
            line=dict(
                color='rgb(44, 62, 80)',
                width=1)
        )
        trace4gyro_IMU = go.Scatter(
            y=gyro_x,
            mode='lines',
            name='gyroX',
            line=dict(
                color='rgb(41, 128, 185)',
                width=1)
        )
        trace5gyro_IMU = go.Scatter(
            y=gyro_y,
            mode='lines',
            name='gyroY',
            line=dict(
                color='rgb(41, 128, 185)',
                width=1)
        )
        trace6gyro_IMU = go.Scatter(
            y=gyro_z,
            mode='lines',
            name='gyroZ',
            line=dict(
                color='rgb(41, 128, 185)',
                width=1)
        )
        trace7mag_IMU = go.Scatter(
            y=mag_x,
            mode='lines',
            name='magX',
            line=dict(
                color='rgb(192, 57, 43)',
                width=1)
        )
        trace8mag_IMU = go.Scatter(
            y=mag_y,
            mode='lines',
            name='magY',
            line=dict(
                color='rgb(192, 57, 43)',
                width=1)
        )
        trace9mag_IMU = go.Scatter(
            y=mag_z,
            mode='lines',
            name='magZ',
            line=dict(
                color='rgb(192, 57, 43)',
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

        filename = dname + ' IMU.html'

        IMU_TrialName = SessionLoc + vicon.GetTrialName()[1] +' ' + filename

        fig['layout'].update(height=2000, width=1800, title=dname + ' IMU Data')

        offline.plot(fig, filename=IMU_TrialName)

    else:
        print('IMU device not found')

print("Graphs Generated - Time Elapsed: {0:.4f} sec".format(time.clock() - start_time))