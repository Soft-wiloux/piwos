import configparser

filename = ".ini"

# Writing Data
config = configparser.ConfigParser()
config.read(filename)

try:
    config.add_section("SETTINGS")
except configparser.DuplicateSectionError:
    pass

config.set("SETTINGS", "language", "piwos")
config.set("SETTINGS", "version", "BETA")
config.set("SETTINGS", "lang", "english")
config.set("SETTINGS", "secondLang", "spanish")
config.set("SETTINGS", "name", "false")

with open(filename, "w") as config_file:
    config.write(config_file)

# Reading Data
config.read(filename)
keys = [
    "language",
    "version",
    "secondLang",
    "lang",
    "name"
]
for key in keys:
    try:
        value = config.get("SETTINGS", key)
        print(f"{key}:", value)
    except configparser.NoOptionError:
        print(f"No option '{key}' in section 'SETTINGS'")