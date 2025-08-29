import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.assets import ArticulationCfg, RigidObjectCfg
from omni.isaac.lab.envs import ManagerBasedRLEnvCfg
from omni.isaac.lab.scene import SceneCfg
from omni.isaac.lab.utils import configclass

##
# Asset Cfg
##

# IMPORTANT: Update this path to your combined UR5e + Hand-E USD file
UR5E_USD_PATH = "/home/aist-eart/ur5e/ur5e_with_gripper.usd" 

# You can use Isaac Sim's built-in assets for the object and basket
CUBE_USD_PATH = "omniverse://localhost/NVIDIA/Assets/Isaac/2023.1.1/Isaac/Props/Blocks/block_instanceable.usd"
BASKET_USD_PATH = "omniverse://localhost/NVIDIA/Assets/Isaac/2023.1.1/Isaac/Environments/Simple_Room/Props/basket.usd"

##
# Main Environment Configuration
##

@configclass
class UR5ePickAndPlaceEnvCfg(ManagerBasedRLEnvCfg):
    """Configuration for the UR5e Pick and Place environment."""

    # Scene Definition
    scene: SceneCfg = SceneCfg(
        # Ground plane
        ground_plane=sim_utils.GroundPlaneCfg(),
        # Distant light
        distant_light=sim_utils.DistantLightCfg(
            intensity=3000.0, color=(0.75, 0.75, 0.75)
        ),
        # Robot asset
        robot=ArticulationCfg(
            prim_path="{ENV_REGEX_NS}/Robot",
            spawn=sim_utils.UsdFileCfg(usd_path=UR5E_USD_PATH),
        ),
        # Object to pick
        object_to_pick=RigidObjectCfg(
            prim_path="{ENV_REGEX_NS}/Object",
            spawn=sim_utils.UsdFileCfg(
                usd_path=CUBE_USD_PATH,
                scale=(0.5, 0.5, 0.5), # Adjust scale as needed
            ),
        ),
        # Basket to place into
        basket=RigidObjectCfg(
            prim_path="{ENV_REGEX_NS}/Basket",
            spawn=sim_utils.UsdFileCfg(usd_path=BASKET_USD_PATH),
        ),
    )

    # We will add Actions, Observations, Rewards, and Randomizations later.
    # This is the minimal setup to just spawn the scene.