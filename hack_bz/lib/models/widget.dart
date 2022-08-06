enum Types{
  control,
  action,
}

class WidgetItem {
  String name;
  Types type;

  WidgetItem(this.name, this.type);

  factory WidgetItem.fromJson(Map<String, dynamic> json) {
    return WidgetItem(
      json['name'],
      json['type'],
    );
  }
}


class DraggableList {
  final String header;
  final List<WidgetItem> items;

  const DraggableList({
    required this.header,
    required this.items,
  });
}

class DraggableListItem {
  final String title;
  final String urlImage;

  const DraggableListItem({
    required this.title,
    required this.urlImage,
  });
}