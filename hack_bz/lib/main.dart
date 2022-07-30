import 'package:flutter/material.dart';
import 'Pages/Home.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Hackaton BZ',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const myHomePage(title: 'Hackaton BZ'),
    );
  }
}