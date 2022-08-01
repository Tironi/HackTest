import 'package:flutter/material.dart';

ThemeData getApplicationTheme(){
  return ThemeData(
    primaryColor: Colors.amber,

    cardTheme: CardTheme(
      elevation: 4,
      color: const Color.fromRGBO(245, 245, 245, 1.0),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(20),
      ),
    ),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        primary: Colors.white,
        textStyle: const TextStyle(color: Colors.black),
        elevation: 4,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
        ),
      ),
    ),
  );
}