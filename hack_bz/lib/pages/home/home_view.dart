import 'dart:async';
import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_staggered_grid_view/flutter_staggered_grid_view.dart';
import 'package:hack_bz/models/processCard.dart';
import 'package:hack_bz/models/widget.dart';
import 'package:hack_bz/widget_view/widget_view.dart';
import 'package:http/http.dart' as http;

part 'package:hack_bz/pages/home/home_controller.dart';

class HomePage extends StatefulWidget {
  HomePage({Key? key}) : super(key: key);

  @override
  _HomePageController createState() => _HomePageController();
}

class _HomePageView extends StatefulView<HomePage, _HomePageController> {
  const _HomePageView(_HomePageController controller, {Key? key})
      : super(controller, key: key);

  @override
  Widget build(BuildContext context) {
    final backgroundColor = Color.fromARGB(255, 243, 242, 248);
    return Scaffold(
      backgroundColor: backgroundColor,
      appBar: AppBar(
        title: const Text("ModulTest"),
        centerTitle: true,
      ),
      body: StaggeredGrid.count(
        crossAxisCount: 4,
        mainAxisSpacing: 4,
        crossAxisSpacing: 4,
        children: [
          StaggeredGridTile.count(
            crossAxisCellCount: 1,
            mainAxisCellCount: 1,
            child: ListView.builder(
                itemCount: controller.lists.length,
                itemBuilder: (context, i) {
                  return Card(
                      child: ListTile(
                          textColor:
                              controller.lists.elementAt(i).type == Types.action
                                  ? Colors.red
                                  : Colors.blue,
                          title: Text(controller.lists.elementAt(i).name),
                          leading: const Icon(Icons.add),
                          onTap: () => controller.onListTileTap(
                              controller.lists.elementAt(i).name,
                              controller.lists.elementAt(i).type)));
                }),
          ),
          StaggeredGridTile.count(
            crossAxisCellCount: 3,
            mainAxisCellCount: 3,
            child: ListView.builder(
                itemCount: controller.processCard.length,
                itemBuilder: (context, index) {
                  return Row(
                    children: <Widget>[
                      Column(children: <Widget>[
                        AnimatedContainer(
                          duration: const Duration(milliseconds: 1000),
                          height: 60,
                          width: 2,
                          color: true ? Colors.red : Colors.blue,
                          child: Container(
                            width: 2,
                            height: 60,
                            color: index == controller.processCard.length - 1
                                ? Colors.white
                                : Colors.black,
                          ),
                        ),
                        Container(
                          margin: const EdgeInsets.only(left: 8, right: 5),
                          padding: const EdgeInsets.all(10),
                          //TODO: cambio il colore
                          decoration: BoxDecoration(
                              color: controller.iconflag == true
                                  ? Colors.green
                                  : Colors.grey,
                              borderRadius: BorderRadius.circular(50)),
                          child: controller.checkicon(),
                        ),
                        Container(width: 2, height: 60, color: Colors.white),
                      ]),
                      Row(
                        children: [
                          Container(
                            width: 300,
                            margin: const EdgeInsets.all(10),
                            decoration: BoxDecoration(
                                color: Colors.white,
                                border: Border(
                                  top: BorderSide(
                                    width: 3,
                                    color: controller.iconflag == true
                                        ? Colors.green
                                        : Colors.grey,
                                  ),
                                  left: BorderSide(
                                    width: 3,
                                    color: controller.iconflag == true
                                        ? Colors.green
                                        : Colors.grey,
                                  ),
                                ),
                                boxShadow: [
                                  BoxShadow(
                                    blurRadius: 5,
                                    color: Colors.black26,
                                  )
                                ]),
                            height: 140,
                            child: Padding(
                              padding: const EdgeInsets.all(10.0),
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: <Widget>[
                                  Text(
                                    controller.processCard[index].title,
                                    style: const TextStyle(
                                        fontSize: 20,
                                        fontWeight: FontWeight.bold,
                                        color: Colors.grey),
                                  ),
                                  Text(
                                    controller.processCard[index].description,
                                    style: const TextStyle(
                                        fontSize: 17, letterSpacing: 2),
                                  ),
                                ],
                              ),
                            ),
                          ),
                          if (controller.processCard[index].type ==
                              Types.action)
                            //TODO
                            //Devo fare due container
                            //Uno per l'input e uno per l'ouput
                            Container(
                              width: 500,
                              height: 140,
                              child: Card(
                                color: Colors.white,
                                child: Container(
                                  padding: EdgeInsets.all(10.0),
                                  child: Column(
                                    children: <Widget>[
                                      Row(
                                        children: <Widget>[
                                          Expanded(
                                            child: Container(
                                              width: 200,
                                              child: Column(
                                                children: [
                                                  TextFormField(
                                                    decoration:
                                                        const InputDecoration(
                                                      hintText: "Input:",
                                                      border: InputBorder.none,
                                                    ),
                                                  ),
                                                ],
                                              ),
                                            ),
                                          ),
                                        ],
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                            ),
                        ],
                      )
                    ],
                  );
                }),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        child: const Icon(Icons.send),
        onPressed: (() {
          controller.setIconflag();
        }),
      ),
    );
  }
}

class WidgetCard extends StatelessWidget {
  WidgetCard(this.name, {Key? key}) : super(key: key);
  late String name;

  @override
  Widget build(BuildContext context) {
    return Card(
      child: const ListTile(
        title: Text("Codesinsider.com"),
      ),
      elevation: 8,
      shadowColor: Colors.green,
      shape: BeveledRectangleBorder(borderRadius: BorderRadius.circular(15)),
    );
  }
}
