import pyrealsense2 as rs
import numpy as np


class DepthCamera() :
    def __init__(self, serialNumber) :
        self.pipeline = rs.pipeline()
        config = rs.config()

        config.enable_device(serialNumber)
        pipeline_wrapper = rs.pipeline_wrapper(self.pipeline)
        self.w = 848
        self.h = 480

        try:
            pipeline_profile = config.resolve(pipeline_wrapper)
            device = pipeline_profile.get_device()
            device_product_line = str(device.get_info(rs.camera_info.product_line))

            config.enable_stream(rs.stream.depth, self.w, self.h, rs.format.z16, 30)
            config.enable_stream(rs.stream.color, self.w, self.h, rs.format.bgr8, 30)

            # Start streaming
            self.pipeline.start(config)
            
            align_to = rs.stream.color
            self.align = rs.align(align_to)
            """ self.depth_to_disparity = rs.disparity_transform(True)
            self.disparity_to_depth = rs.disparity_transform(False)
            
            self.decimation = rs.decimation_filter()
            self.decimation.set_option(rs.option.filter_magnitude, 4)
            
            self.spatial = rs.spatial_filter()
            self.spatial.set_option(rs.option.filter_magnitude, 5)
            self.spatial.set_option(rs.option.filter_smooth_alpha, 1)
            self.spatial.set_option(rs.option.filter_smooth_delta, 50)
            self.spatial.set_option(rs.option.holes_fill, 3)
            
            self.temporal = rs.temporal_filter()
            self.hole_filling = rs.hole_filling_filter()  """
            self.status = True
        except:
            self.status = False

    def getFrame(self, filters = False) :
        try:
            frames = self.pipeline.wait_for_frames()
            aligned_frames = self.align.process(frames)
        
            depth_frame = aligned_frames.get_depth_frame()
            color_frame = aligned_frames.get_color_frame()
            
            if filters:
                depth_frame = self.decimation.process(depth_frame)
                depth_frame = self.depth_to_disparity.process(depth_frame)
                depth_frame = self.spatial.process(depth_frame)
                depth_frame = self.temporal.process(depth_frame)
                depth_frame = self.disparity_to_depth.process(depth_frame)
                depth_frame = self.hole_filling.process(depth_frame)

            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())
            if not depth_frame or not color_frame :
                return False, None, None, None
            return True, depth_image, color_image, None
        except:
            return False, None, None, None
        
    def release(self) :
        self.pipeline.stop()