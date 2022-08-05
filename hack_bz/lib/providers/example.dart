
import 'package:flutter/material.dart';
import 'package:hack_bz/models/parking_spots.dart';

class ModelSelectedParks with ChangeNotifier {
  final List<ParkingSpot> _listParks = [
    ParkingSpot(
        type: "Sosta libera",
        icon: 'assets/icon/sosta_libera.svg',
        isSelected: true),
    ParkingSpot(
        type: "Sosta a tempo",
        icon: 'assets/icon/sosta_tempo.svg',
        isSelected: true),
    ParkingSpot(
        type: "Sosta a pagamento",
        icon: 'assets/icon/sosta_pagamento.svg',
        isSelected: true),
    ParkingSpot(
        type: "Disabili",
        icon: 'assets/icon/sosta_disabili.svg',
        isSelected: true),
    ParkingSpot(
        type: "Veicoli elettrici",
        icon: 'assets/icon/sosta_elettrici.svg',
        isSelected: true),
    ParkingSpot(
        type: "Moto", icon: 'assets/icon/sosta_moto.svg', isSelected: false),
    ParkingSpot(
        type: "Residenti",
        icon: 'assets/icon/sosta_residenti.svg',
        isSelected: false),
    ParkingSpot(
        type: "Altro", icon: 'assets/icon/sosta_altro.svg', isSelected: false),
  ];
  //List<ParkingSpot> _listSelectedParks = [];

  void selectParkingSpot(int index) {
    _listParks[index].isSelected = true;
    notifyListeners();
  }

  void deselectParkingSpot(int index) {
    _listParks[index].isSelected = false;
    notifyListeners();
  }

  void reset() {
    for (ParkingSpot p in _listParks) {
      p.isSelected = false;
    }
    listParks[0].isSelected = true;
    listParks[1].isSelected = true;
    listParks[2].isSelected = true;
    listParks[3].isSelected = true;
    listParks[4].isSelected = true;
    notifyListeners();
  }

  //void addPark(ParkingSpot p) {
  //  _listSelectedParks.add(p);
//
  //  notifyListeners();
  //}
//
  //void removePark(ParkingSpot p) {
  //  _listSelectedParks.remove(p);
  //  notifyListeners();
  //}
//
  //void removeAll() {
  //  _listSelectedParks.clear();
  //  _listSelectedParks.add(_listParks[0]);
  //  notifyListeners();
  //}
//
  //List<ParkingSpot> get selectedParks => _listSelectedParks;
  List<ParkingSpot> get listParks => _listParks;
//
  ///given an index it returns if the [ParkingSpot] at that position in [_listParks] is selected or not
  bool isParkSelected(int index) {
    return _listParks[index].isSelected;
  }

  bool isParkingCategorySelected(String? category) {
    for (ParkingSpot p in _listParks) {
      if (p.type == category) {
        return p.isSelected;
      }
    }
    return false;
  }
}
