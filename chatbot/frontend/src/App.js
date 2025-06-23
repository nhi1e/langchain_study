import { useState } from "react";
import axios from "axios";

function App() {
	const [messages, setMessages] = useState([]);
	const [input, setInput] = useState("");
	const [userId, setUserId] = useState("u001");
	const [loading, setLoading] = useState(false);

	const handleSend = async () => {
		if (!input.trim()) return;

		const newMessage = { sender: "user", text: input };
		setMessages((prev) => [...prev, newMessage]);
		setLoading(true);

		console.log("Sending request:", { user_id: userId, message: input });

		try {
			const res = await axios.post("http://localhost:8000/chat", {
				user_id: userId,
				message: input,
			});

			console.log("Response from backend:", res.data);

			const botMessage = {
				sender: "bot",
				text: res.data.response,
				source: res.data.query_type,
			};

			setMessages((prev) => [...prev, botMessage]);
		} catch (err) {
			console.error("Request failed:", err);
			setMessages((prev) => [
				...prev,
				{ sender: "bot", text: "Something went wrong." },
			]);
		} finally {
			setInput("");
			setLoading(false);
		}
	};
  
	return (
		<div className="max-w-xl mx-auto mt-10 p-4 border rounded-xl shadow">
			<h1 className="text-2xl font-bold mb-4">Tech Support Chatbot</h1>
			<div className="space-y-2 mb-4 max-h-96 overflow-y-auto">
				{messages.map((msg, idx) => (
					<div
						key={idx}
						className={`p-2 rounded-lg ${
							msg.sender === "user"
								? "bg-blue-100 text-right"
								: "bg-gray-100 text-left"
						}`}
					>
						<p className="whitespace-pre-line">{msg.text}</p>
						{msg.source && (
							<p className="text-xs text-gray-500 italic">
								Source: {msg.source}
							</p>
						)}
					</div>
				))}
			</div>

			<div className="flex gap-2">
				<input
					className="flex-1 border rounded-lg p-2"
					value={input}
					onChange={(e) => setInput(e.target.value)}
					onKeyDown={(e) => e.key === "Enter" && handleSend()}
					placeholder="Ask a question..."
				/>
				<button
					onClick={handleSend}
					className="bg-blue-500 text-white px-4 py-2 rounded-lg"
					disabled={loading}
				>
					{loading ? "..." : "Send"}
				</button>
			</div>
		</div>
	);
}

export default App;
