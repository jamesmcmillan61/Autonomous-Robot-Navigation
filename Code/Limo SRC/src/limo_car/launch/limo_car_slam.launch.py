from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg_share = FindPackageShare('limo_car')
    sim_launch = PathJoinSubstitution([pkg_share, 'launch', 'limo_car_sim.launch.py'])
    slam_params = PathJoinSubstitution([pkg_share, 'config', 'slam_toolbox.yaml'])

    return LaunchDescription([
        IncludeLaunchDescription(PythonLaunchDescriptionSource(sim_launch)),
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[slam_params],
        ),
    ])
