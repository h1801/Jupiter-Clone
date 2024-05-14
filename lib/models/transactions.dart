import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:uuid/uuid.dart';

final db = FirebaseFirestore.instance;

class Transactions {
  final DateTime date;
  final num amount;
  final String description;
  final String category;
  Transactions(this.date, this.amount, this.description, this.category);

  Map<String, dynamic> toMap() {
    return {
      'date': date,
      'amount': amount,
      'description': description,
      'category': category
    };
  }
}
