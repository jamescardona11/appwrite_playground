import { throwIfMissing } from './utils.js';

export default async ({ req, res, log, error }) => {


  if (req.method === 'GET') {
    log('GET request');
    return res.json({ ok: false, response: 'Hello!!' }, 200);
  }

  try {
    throwIfMissing(req.body, ['input']);
  } catch (err) {
    error(err.message);
    return res.json({ ok: false, error: err.message }, 400);
  }

  try {

    const input = req.body.input;
    log(`input : ${input}`);

    let firstIndex = input.indexOf('[');
    let realInput = input.substring(firstIndex, input.length - 1);
    let output = realInput.replace(/[\[\]{},"]/g, '');
    let list = output.split("tweet:");
    let response = JSON.stringify(list.filter(e => e.trim().length > 0).map(e => e.trim()).join('-*-*-'));

    log(`response : ${response}`);


    return res.json({ ok: true, response: response }, 200);
  } catch (err) {
    error(err);
    return res.json({ ok: false, err: err }, 400);
  }
};

