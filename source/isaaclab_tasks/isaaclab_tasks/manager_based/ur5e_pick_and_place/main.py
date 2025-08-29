import argparse
from omni.isaac.lab.app import AppLauncher

# Add argparse wrapper for launching from command line
parser = argparse.ArgumentParser(description="UR5e Pick and Place environment.")
AppLauncher.add_app_launcher_args(parser)
args_cli = parser.parse_args()

# Launch Isaac Sim
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab_tasks.environments.ur5e_pick_and_place import UR5ePickAndPlaceEnv, UR5ePickAndPlaceEnvCfg


def main():
    """Main function to create and run the environment."""

    # Create an instance of the environment configuration
    env_cfg = UR5ePickAndPlaceEnvCfg(num_envs=16, env_spacing=2.0)

    # Create the environment
    env = UR5ePickAndPlaceEnv(cfg=env_cfg)

    # Get the simulation context
    sim = sim_utils.SimulationContext(
        physics_dt=env.physics_dt, rendering_dt=env.rendering_dt, backend="torch"
    )

    # Reset the environment at the start
    env.reset()
    print("Environment reset.")

    # Run the simulation loop
    while simulation_app.is_running():
        # Step the simulation
        with sim.step():
            # Step the environment
            # In the future, we will pass real actions here
            env.step(env.action_manager.get_default_action())
    
    # Close the environment
    env.close()


if __name__ == "__main__":
    main()
    # Close the simulation
    simulation_app.close()