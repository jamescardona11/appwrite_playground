import 'dart:async';
import 'dart:convert';

Future<dynamic> main(final context) async {
  if (context.req.method == 'GET') {
    return context.res.json({'ok': true, 'response': ''}, 200);
  }

  final input = context.req.body['input'];

  try {
    context.log('Input to generate: $input');

    String output = input.replaceAll(RegExp(r'[\[\]{},"]'), '');
    final list = output.split("tweet:");

    final response = jsonEncode(list.where((e) {
      return e.isNotEmpty;
    }).map((e) {
      return e.trim();
    }).join('-*-*-'));

    context.log('Response: $response');

    return context.res.json({'ok': true, 'response': response}, 200);
  } catch (err) {
    context.log(err);
    return context.res.json({'ok': false, 'response': ''}, 400);
  }
}
