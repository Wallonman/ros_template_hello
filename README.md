# Base template for a minimal ROS2 package

## Prerequisites

This sample template supposes that ROS2 has been installed on a linux (Ubuntu 20.04) following the ROS2 [documentation](https://docs.ros.org/en/galactic/)

## Source the ROS2 instalation as underlay of the package

``` bash
source ~/ros2_galactic/ros2-linux/setup.bash
```

## Setup the workspace and create the package

Create the workspace folder and the `src` sub-folder where the package will be created

``` bash
mkdir -p ~/template_ws/src
cd ~/template_ws/src/
```
> The workspace will be called `template_ws`


Create the package in the `src` sub-folder

``` bash
ros2 pkg create --build-type ament_python hello_py_pkg
```
> The folder structure and files are generated, the package is called `hello_py_pkg`

> Note the `./hello_py_pkg/hello_py_pkg` folder where the Python code of the nodes will be created later

## Create the publisher and subscriber nodes and build

Create the Python files `publisher.py` and `subscriber.py` under the `./hello_py_pkg/hello_py_pkg` write the code like the sample [](hello_py_pkg/hello_py_pkg/publisher.py)




