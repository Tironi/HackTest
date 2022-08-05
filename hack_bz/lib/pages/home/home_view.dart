import 'package:flutter/material.dart';
import 'package:hack_bz/widget_view/widget_view.dart';


part 'package:hack_bz/pages/home/home_controller.dart';

class HomePage extends StatefulWidget {

  final String name;
  const HomePage(this.name, {Key? key}) : super(key: key);

  @override
  _HomePageController createState() => _HomePageController();
}

class _HomePageView extends StatefulView<HomePage, _HomePageController> {
  
  const _HomePageView(_HomePageController controller, {Key? key, String? name}) : super(controller, key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      child: [
        
      ],
    );
  }
}
