import 'package:flutter/material.dart';
import 'package:hack_bz/models/widget.dart';

class ProcessCard{
  String title;
  String description;
  Types type;
  IconData icon;

  ProcessCard(this.title, this.description, this.icon, this.type);
}