#include <iostream>

#include "opencv2/opencv.hpp"

#include "rosbag-reader/rosbag_reader.h"

void onRosImage(sensor_msgs::Image::ConstPtr imageMsg)
{
	auto imagePtr = cv_bridge::toCvCopy(imageMsg, sensor_msgs::image_encodings::BGR8);
	if (imagePtr->image.empty())
		return;
	cv::imshow("im", imagePtr->image);
	cv::waitKey(15);
}

int main(int agrc, char** argv)
{
	std::cout << "Generated main program for project: rosbag-reader-driver" << std::endl;

	RosbagReader r("/home/dan/ml/dat/vehicle_images_04_02/2021-03-27-11-49-03.bag", 0, 0);

	auto b = std::bind(&onRosImage, std::placeholders::_1);

	r.setImageTopn("/image_raw");
	r.setImageCallback(b);

	r.start();

	return 0;
}