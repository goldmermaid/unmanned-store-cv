# A Full Computer Vision Pipeline of the Unmanned Store

An [unmanned store](https://en.wikipedia.org/wiki/Unmanned_store) is a retail concept in which there are no service personnel and no cashiers in the store. The transactions are handled through a mobile application. A great example of an unmanned store is the [Amazon Go](https://www.amazon.com/b/ref=s9_acss_bw_cg_agojwo_1b1_w?node=20931384011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=0JDH7W3PYZE63NJSDS4Z&pf_rd_t=101&pf_rd_p=202bb5f6-3afe-4534-ad20-9eb246c4051a&pf_rd_i=16008589011).

In this project, we will work on an end-to-end computer vision (CV) system: a mini Unmanned Store. Our system is able to automaticly detect whether any object is grabbed from a shelf in a real-time fashion.


## I. Getting Started

### Example of Training and Test

1. YOLO based Models
     [src/training_object_detector_yolo3.ipynb](src/training_object_detector_yolo3.ipynb) and [src/test_object_detector_yolo3.ipynb](src/test_object_detector_yolo3.ipynb) (Yolo3, Recommended)

1. SSD based Models
     [src/training_object_detector.ipynb](src/training_object_detector.ipynb) and [src/test_object_detector.ipynb](src/test_object_detector.ipynb) (SSD)

### Testing Results
After the training, your model should be able to detect the objects such as "noodles", "hand", etc.

<img height="200" alt="portfolio_view" src="images/demo/demo2.png">
<img height="200" alt="portfolio_view" src="images/demo/demo3.png">
<img height="200" alt="portfolio_view" src="images/demo/demo4.png">
<img height="200" alt="portfolio_view" src="images/demo/demo5.png">






## II. Computer Vision Hackathon: Mini Amazon Go

### Date: 2019.10


### Hardware

- [Raspberry Pi 4](https://www.amazon.com/gp/product/B07TXMDVPQ/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

<img height="200" alt="portfolio_view" src="https://user-images.githubusercontent.com/3307514/66869709-c7ce7b00-ef54-11e9-8824-32cbcd40100d.png">

- [camera module](https://www.amazon.com/gp/product/B07PQ63D2S/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)

<img height="200" alt="portfolio_view" src="https://user-images.githubusercontent.com/3307514/66869685-b8e7c880-ef54-11e9-969c-2ed21178d7ca.png">

- [touch screen + protection case](https://www.amazon.com/gp/product/B07WRV48ZW/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)

### AWS Kinesis Video Stream on Raspberry Pi

Tutorial: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi.html

#### Notes

- The default region is `us-west-2`. Change to nearest region if applicable.
- Raspbian OS can use `apt-get` to install shared libs to accelerate compilation of Kinesis Producer C++ SDK (https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/blob/master/install-instructions-linux.md#install-steps-for-ubuntu-17x-and-raspbian-stretch-using-apt-get)
- Setup IAM role for Kinesis Video Stream, and paste the secret key to raspberry
- There's a sample app to upload videos to KVS.
`./kinesis_video_gstreamer_sample_app -w <width> -h <height> -f <framerate> -b <bitrateInKBPS> Stream Name` (Note that not all resolution works, 640x480 works on Raspberry Pi 4 for me), or you can use [src/start_upload.sh](src/start_upload.sh).

#### Trouble shooting

There's potential fix for large latency: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/troubleshooting.html#troubleshooting-general

### SageMaker Notebook

#### Access Permission

For SageMaker notebook to access KVS, it must have permission `AmazonKinesisVideoStreamsFullAccess` added to the SageMaker Execution Role when creating the notebook instance

#### Example notebook for processing KVS

See [VideoStream Example](src/VideoStream.ipynb).


### References:

[Beijing CV hackathon](https://github.com/hetong007/d2l-1day-cv-hackathon)

