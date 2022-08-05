import 'package:flutter/material.dart';

class ParkingSpot {
  final String type;
  final String icon;
  bool isSelected;

  ParkingSpot(
      {required this.type, required this.icon, required this.isSelected});
}
