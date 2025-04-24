"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export const QueryAnswering = () => {
  const [messages, setMessages] = useState<
    { sender: "user" | "ai"; text: string }[]
  >([]);
  const [currentQuery, setCurrentQuery] = useState("");

  const handleAskWicketWise = () => {
    if (currentQuery.trim() === "") return;

    // Add user's query to the chat
    setMessages([...messages, { sender: "user", text: currentQuery }]);

    // Simulate AI response (replace with actual LLM call)
    setTimeout(() => {
      const aiResponse = `This is a mock response to "${currentQuery}".`;
      setMessages([...messages, { sender: "user", text: currentQuery }, { sender: "ai", text: aiResponse }]);
    }, 500);

    setCurrentQuery("");
  };

  return (
    <Card className="space-y-4">
      <CardHeader>
        <CardTitle>💬 Query Answering</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="h-64 overflow-y-auto space-y-2">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`p-2 rounded-md ${
                message.sender === "user" ? "bg-secondary text-secondary-foreground self-end" : "bg-muted text-muted-foreground self-start"
              }`}
            >
              {message.text}
            </div>
          ))}
        </div>
        <div className="flex space-x-2">
          <Input
            type="text"
            placeholder="Ask WicketWise"
            value={currentQuery}
            onChange={(e) => setCurrentQuery(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleAskWicketWise();
              }
            }}
          />
          <Button onClick={handleAskWicketWise}>Ask WicketWise</Button>
        </div>
      </CardContent>
    </Card>
  );
};
