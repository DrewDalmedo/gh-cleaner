{ pkgs, lib, config, inputs, ... }:

{
  languages.python = {
    enable = true;

    venv = {
      enable = true;
      requirements = ''
        PyGithub
      '';
    };
  };

  dotenv.enable = true;
}
