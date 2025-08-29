from omni.isaac.lab.envs import ManagerBasedRLEnv

from .config.ur5e_pick_and_place_cfg import UR5ePickAndPlaceEnvCfg

class UR5ePickAndPlaceEnv(ManagerBasedRLEnv):
    """
    This class is the main environment for the UR5e pick and place task.
    It will be expanded later to handle actions, observations, and rewards.
    """

    def __init__(self, cfg: UR5ePickAndPlaceEnvCfg, **kwargs):
        """Initialize the environment."""
        # Pass the configuration to the parent class
        super().__init__(cfg=cfg, **kwargs)