import yaml

config = {}
with open("/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# TODO: Check config
