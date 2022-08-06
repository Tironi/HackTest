import 'dart:async';
import 'dart:convert';
import 'package:hack_bz/models/widget.dart';

import 'package:http/http.dart' as http;


Future<WidgetItem> fetchAlbum() async {
  final response = await http.
    get(Uri.parse('https://jsonplaceholder.typicode.com/albums/1'));

    var body = jsonEncode({ 'data': { "array": [ {"id": "0", "param": ["Iphone 3", "Iphone 2"] } ]
} });

  if (response.statusCode == 200) {
    // If the server did return a 200 OK response,
    // then parse the JSON.
    return WidgetItem.fromJson(jsonDecode(response.body));
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to load widget');
  }
}