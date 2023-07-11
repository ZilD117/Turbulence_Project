import os

def read_config(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def write_config(file_path, config):
    with open(file_path, 'w') as file:
        for line in config:
            file.write(line + '\n')

def replace_param(config, param_name, new_value):
    for i in range(len(config)):
        if config[i].startswith(param_name):
            # Split on = and replace the value
            parts = config[i].split('=')
            parts[1] = ' ' + str(new_value)   # We add a space before the new value for formatting
            config[i] = '='.join(parts)
    return config

# Load the original parameters file
original_config = read_config('./turbulence.in')  # Replace with your file path

# Dictionary of new values for each parameter
new_values_dict = {
    'b0': [0.00001,0.0001,0.001, 0.1,1.0,10.0],
    'b_config': [0,1,4],
    'accel_rms': [0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0]
}

# Loop through each parameter in the dictionary
for param in new_values_dict:
    # Loop through each new value for this parameter
    for new_value in new_values_dict[param]:
        # Copy the original configuration
        new_config = original_config.copy()

        # Replace the parameter with the new value
        new_config = replace_param(new_config, param, new_value)

        # Create a new directory for this configuration
        new_dir_path = './changed/{}_{}'.format(param, new_value)  # Replace with your directory path
        os.makedirs(new_dir_path, exist_ok=True)

        # Save the new configuration to a new .in file in the new directory
        new_file_path = os.path.join(new_dir_path, 'turbulence.in')
        write_config(new_file_path, new_config)
