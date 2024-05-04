import 'dart:async';
import 'dart:io';
import 'package:google_generative_ai/google_generative_ai.dart';

import 'utils.dart';


Future<dynamic> main(final context) async {
  throwIfMissing(Platform.environment, ['GEMINI_API_KEY']);

  if (context.req.method == 'GET') {
    return context.res.json({'ok': true, 'response': ''}, 200);
  }

  try {
    throwIfMissing(context.req.body, ['prompt']);
  } catch (err) {
    return context.res.json({'ok': false, 'error': err.toString()});
  }

  const apiKey = Platform.environment['GEMINI_API_KEY']!;
  final prompt = context.req.body['prompt'];

  try {

    final model = GenerativeModel(model: 'gemini-pro', apiKey: apiKey);
    final response = await model.generateContent([Content.text(system + prompt)]);

    return context.res.json({'ok': true, 'response': response.text}, 200);
  } on RequestFailedException {
    return context.res.json({'ok': false, 'response', '');
  }
}
