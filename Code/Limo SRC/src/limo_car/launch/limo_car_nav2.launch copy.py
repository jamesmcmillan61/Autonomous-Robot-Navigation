from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    limo_share = FindPackageShare('limo_car')
    nav2_share = FindPackageShare('nav2_bringup')

    sim_launch = PathJoinSubstitution([limo_share, 'launch', 'limo_car_sim.launch.py'])

    map_file = PathJoinSubstitution([limo_share, 'maps', 'OwnInit.yaml'])
    params_file = PathJoinSubstitution([limo_share, 'config', 'nav2_params.yaml'])

    nav2_launch = PathJoinSubstitution([nav2_share, 'launch', 'bringup_launch.py'])

    return LaunchDescription([
        IncludeLaunchDescription(PythonLaunchDescriptionSource(sim_launch)),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(nav2_launch),
            launch_arguments={
                'slam': 'False',
                'map': map_file,
                'use_sim_time': 'True',
                'params_file': params_file,
                'autostart': 'True',
            }.items()
        ),
    ])
