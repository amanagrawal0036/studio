"use client";

import React, { createContext, useContext, useState } from "react";

type Insight = {
  type: string;
  query: string;
  result: string;
};

type Query = {
  query: string;
  response: string;
};

type DashboardContextType = {
  insights: Insight[];
  queries: Query[];
  addInsight: (insight: Insight) => void;
  addQuery: (query: Query) => void;
};

const DashboardContext = createContext<DashboardContextType | undefined>(undefined);

export const DashboardProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [insights, setInsights] = useState<Insight[]>([]);
  const [queries, setQueries] = useState<Query[]>([]);

  const addInsight = (insight: Insight) => {
    setInsights([...insights, insight]);
  };

  const addQuery = (query: Query) => {
    setQueries([...queries, query]);
  };

  const value: DashboardContextType = {
    insights,
    queries,
    addInsight,
    addQuery,
  };

  return (
    <DashboardContext.Provider value={value}>
      {children}
    </DashboardContext.Provider>
  );
};

export const useDashboardContext = () => {
  const context = useContext(DashboardContext);
  if (!context) {
    throw new Error("useDashboardContext must be used within a DashboardProvider");
  }
  return context;
};
