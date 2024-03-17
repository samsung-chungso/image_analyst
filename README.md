# 사용한 기술

### Deep Learning model package
#### Road Extraction - Global
##### Input
8-bit, 3-band high resolution (1 meter) aerial/satellite imagery.
##### Output
Feature class representing road network. 
##### Model architecture
The implementation is based on the Sat2Graph model by Songtao He, et al. 
##### Metrics
The model has an F1 score of 76.26 on city-scale dataset. It has a precision of 0.807 and recall of 0.723

This deep learning model is used to extract roads from high resolution (1 meter) aerial/satellite imagery. Road layers are useful in preparing base maps and analysis workflows for urban planning and development, change detection, infrastructure planning, and a variety of other applications.

Digitizing roads from imagery is a time-consuming task and is commonly done by digitizing features manually. Deep learning models are highly capable of learning these complex semantics and can produce superior results. Use this deep learning model to automate this process and reduce the time and effort required for acquiring road layers.

### Object extraction from image
![image](https://github.com/samsung-chungso/image_analyst/assets/103614665/82a129f2-7256-4112-aee5-d3bc70ce2fa8)
Runs a trained deep learning model on an input raster to produce a feature class containing the objects it finds. The features are polyline of the objects.

We used Detect Objects Using Deep Learning tool which requires a model definition file containing trained model information. The model was trained using the TensorFlow. The model definition file was a deep learning model package, and it contains the path to the Python raster function to be called to process each object and the path to the trained binary deep learning model file.

#### Further…

### Automatic road extraction using deep learning
- 타 대학 캠퍼스 도로 추출 및 서비스 확대
- 도로 추출 워크플로 자동화
