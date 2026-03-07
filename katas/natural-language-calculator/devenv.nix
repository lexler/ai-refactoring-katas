{ pkgs, inputs, ... }:

{
  languages.python = {
    enable = true;
    version = "3.12";
  };

  packages = [
    pkgs.uv
    pkgs.bat
    pkgs.viddy
    inputs.yaks.packages.${pkgs.system}.default
  ];
}
