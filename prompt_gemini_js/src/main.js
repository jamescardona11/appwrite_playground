import { GoogleGenerativeAI } from "@google/generative-ai";
import { system, throwIfMissing } from './utils.js';



export default async ({ req, res, log, error }) => {
  throwIfMissing(process.env, ['GEMINI_API_KEY']);

  if (req.method === 'GET') {
    log('GET request');
    return res.json({ ok: false, response: 'Hello!!' }, 200);
  }

  try {
    throwIfMissing(req.body, ['prompt']);
  } catch (err) {
    error(err.message);
    return res.json({ ok: false, error: err.message }, 400);
  }

  const api = process.env.GEMINI_API_KEY;
  log(`API Key: ${api}`);

  try {
    const genAI = new GoogleGenerativeAI(api);
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });

    const prompt = req.body.prompt;

    log(`Generating content for prompt: ${prompt}`);
    log(`Using model: ${system + prompt}`);

    const result = await model.generateContent(system + prompt);
    const response = await result.response;
    const text = response.text();
    log(`Generated content: ${text}`);
    return res.json({ ok: true, response: text }, 200);
  } catch (err) {
    error(err);
    return res.json({ ok: false, err: err }, 400);
  }
};

