{
  description = "Build dependencies flake";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };
  outputs = { self, nixpkgs }:
  let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in
  {
    devShells.${system}.default = pkgs.mkShell {
      buildInputs = with pkgs; [
        (python314.withPackages (p: with p; [
          pandas
          seaborn
          numpy
        ]))
        texliveFull
        gnuplot
      ];
      shellHook = ''
        export PYTHONPATH="$(pwd)"
        zsh
      '';
    };
  };
}
