import yaml
import yamale
import sys

def load_config(config_file):
    """Loads and parses the YAML configuration file."""
    with open(config_file, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"Error loading YAML file: {exc}")
            sys.exit(1)

def validate_config(schema_file, config_file):
    """Validates the configuration file against the schema."""
    try:
        schema = yamale.make_schema(schema_file)
        data = yamale.make_data(config_file)
        yamale.validate(schema, data)
        print(f"{config_file} is valid!")
    except Exception as e:
        print(f"Validation failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    schema_file = 'config_schema.yaml'
    config_file = 'config.yml'

    # Validate the config file
    validate_config(schema_file, config_file)
