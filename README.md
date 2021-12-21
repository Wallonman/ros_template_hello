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

# create the package and a first node (hello_py_pkg/hello_py_pkg/pubisher.py will be created)
ros2 pkg create --build-type ament_python hello_py_pkg --node-name publisher
```
> The folder structure and files are generated, the package is called `hello_py_pkg`

> Note the `./hello_py_pkg/hello_py_pkg` folder where the Python code of the nodes will be created later

## Create the publisher and subscriber nodes

Create the Python files `publisher.py` and `subscriber.py` under the `./hello_py_pkg/hello_py_pkg` write the code like the sample [publisher.py](hello_py_pkg/hello_py_pkg/publisher.py) and [subscriber.py](hello_py_pkg/hello_py_pkg/subscriber.py)

## Add entry points

Look to the [setup.py](hello_py_pkg/setup.py)  to add the entry points for both publisher and subscriber

## Finally let's build, install and run

Now you can build.
> The build must be launched from the workspace's root

``` bash
colcon build

or

colcon build --packages-select hello_py_pkg
```

Install (source) the package locally, from the worskpace folder, and run the publisher...

``` bash
# source the setup files from inside the template_ws
. install/local_setup.bash

# And now ... run the publisher
ros2 run hello_py_pkg publisher
```

... and run the subscriber in another terminal

``` bash
# source the setup files from inside the template_ws
. install/local_setup.bash

# And now ... run the subscriber
ros2 run hello_py_pkg subscriber
```

## Get some package information

``` bash
# list packages
ros2 pkg executables hello_py_pkg

# get package info
ros2 pkg executables hello_py_pkg
```




