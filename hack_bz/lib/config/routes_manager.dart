import 'package:flutter/material.dart';
import 'package:hack_bz/pages/home/home_view.dart';

class Routes{
  static const String home = "/";
}

class RouteGenerator {
  static Route<dynamic> getRoute(RouteSettings routeSettings){
    switch(routeSettings.name){
      case Routes.home:
        return MaterialPageRoute(builder: (_)=> HomePage());
      default:
        return unDefinedRoute();
    }
  }

  static Route<dynamic> unDefinedRoute(){
    return MaterialPageRoute(builder: (_)=>
      Scaffold(
        appBar: AppBar(title: const Text("Nessuna rotta trovata"), ),
        body: const Text("Nessuna rotta trovata"),
      )
    );
  }
}

