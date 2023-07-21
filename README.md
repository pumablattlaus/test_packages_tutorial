# Test ROS Packages Tutorial

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>
Example package for ROS-testing the package and implementing a github workflow.


## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites
- ROS noetic
- rostest

### Installing

1. Clone repo into catkin_ws/src
2. build ws

Add own remote to see github workflow after pushing.

## Usage <a name = "usage"></a>

For running the example test via command line:
```
rostest test_packages_tutorial load_param.test
```

For changing how and when github is testing the package: Modify [ci-focal-action.yml](.github/workflows/ci-focal-action.yml)