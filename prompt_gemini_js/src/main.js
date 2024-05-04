import { GoogleGenerativeAI } from "@google/generative-ai";
import { system, throwIfMissing } from './utils.js';



export default async ({ req, res }) => {
  throwIfMissing(process.env, ['GEMINI_API_KEY']);

  if (req.method === 'GET') {
    return res.json({ ok: false, response: '' }, 200);
  }

  try {
    throwIfMissing(req.body, ['prompt']);
  } catch (err) {
    return res.json({ ok: false, error: err.message }, 400);
  }

  const api = process.env.GEMINI_API_KEY;

  try {
    const genAI = new GoogleGenerativeAI(api);
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });

    const prompt = req.body.prompt;

    const result = await model.generateContent(system + prompt);
    const response = await result.response;
    const text = response.text();
    return res.json({ ok: true, response: text }, 200);
  } catch (err) {
    return res.json({ ok: false, response: '' }, 200);
  }
};


async function main() {



};


main()