void main(List<String> args) {
  Map<String, dynamic> mappa = {
    "articolo": [
      {"ciao": "tiru"},
      {"ciao": "mondo"},
      {"ciao": "mondo"},
    ]
  };

  for (int i = 0; i < 3; i++) {
    mappa['articolo'][i] = {"ciao": "mondo"};
  }
  print(mappa);
}
