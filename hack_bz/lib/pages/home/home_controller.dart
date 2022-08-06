part of 'package:hack_bz/pages/home/home_view.dart';

class _HomePageController extends State<HomePage> {

  List<ProcessCard> processCard = [];
  List<ProcessCard> _getProcess(){
      List<ProcessCard> processCard = [];
      return processCard;
  }  

  List<WidgetItem> lists = [];
  List<WidgetItem> _getLists(){
      List<WidgetItem> lists = [];

      lists.add(
        WidgetItem(
          'Seleziona device',
        Types.control)
      );      
      lists.add(
        WidgetItem(
          'Aggiungi device al carrello',
        Types.control)
      );
      lists.add(
        WidgetItem(
          'Visualizza carrello',
        Types.control)
      );
      lists.add(
        WidgetItem(
          'Controllo carrello',
        Types.action)
      );
      return lists;
  }

  @override
  Widget build(BuildContext context) => _HomePageView(this);

  @override
  void initState() {
    lists = _getLists();
    processCard = _getProcess();
  }

  Widget test(){
    return const Text("ciao");
  }

  void onListTileTap(String name, Types tipo){
    setState(() {
      processCard.add(ProcessCard(name, "Descrizione", Icons.hourglass_bottom, tipo));
    });
  }


  push() async {
    processCard.forEach((element) {

    });
  }
}