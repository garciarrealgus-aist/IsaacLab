"""Entrypoint for the UR5e pick and place environment."""

from .ur5e_pick_and_place_env import UR5ePickAndPlaceEnv, UR5ePickAndPlaceEnvCfg

# Register the environment with the Isaac Lab environment registry
import omni.isaac.lab_tasks.config  # noqa: F401