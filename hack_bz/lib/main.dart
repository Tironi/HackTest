import 'package:flutter/material.dart';

import 'package:hack_bz/config/routes_manager.dart';
import 'package:hack_bz/config/theme_manager.dart';

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
      theme: getApplicationTheme(),
        
      initialRoute: Routes.home,
      onGenerateRoute: RouteGenerator.getRoute,
   
    );
  }
}
