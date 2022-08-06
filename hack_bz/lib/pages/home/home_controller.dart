part of 'package:hack_bz/pages/home/home_view.dart';

class _HomePageController extends State<HomePage> {
  List<ProcessCard> processCard = [];
  List<ProcessCard> _getProcess() {
    List<ProcessCard> processCard = [];
    return processCard;
  }

  bool iconflag = false;

  List<WidgetItem> lists = [];
  List<WidgetItem> _getLists() {
    List<WidgetItem> lists = [];

    lists.add(WidgetItem('Select device', Types.control, "ajnldsanjd "));
    lists.add(WidgetItem('Add to cart', Types.control, "fdsf"));
    lists.add(WidgetItem('view cart', Types.control, "fj"));
    lists.add(WidgetItem('check cart', Types.action, "fealfe"));
    return lists;
  }

  @override
  Widget build(BuildContext context) => _HomePageView(this);

  @override
  void initState() {
    lists = _getLists();
    processCard = _getProcess();
  }

  Widget test() {
    return const Text("ciao");
  }

  void onListTileTap(String name, Types tipo) {
    setState(() {
      processCard.add(
          ProcessCard(0, name, "descitption", Icons.hourglass_bottom, tipo));
    });
  }

  void sendtoPython(ProcessCard card) {
    var a = new Map();
  }

  push() async {
    processCard.forEach((element) {});
  }

  void setIconflag() {
    setState(() {
      iconflag = true;
    });
  }
}
