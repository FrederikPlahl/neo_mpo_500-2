from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution


def generate_launch_description():
   

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('neo_mpo_500-2'),
                    'launch',
                    'bringup.launch.py'
                ])
            ])
    
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('neo_mpo_500-2'),
                    'launch',
                    'navigation.launch.py'
                ])
            ])
    
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('neo_mpo_500-2'),
                    'launch',
                    'rviz.launch.py'
                ])
            ])
    
        )
    ])
