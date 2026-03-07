{ pkgs, ... }:

{
  languages.python = {
    enable = true;
    version = "3.12";
  };

  packages = [
    pkgs.uv
  ];
}
