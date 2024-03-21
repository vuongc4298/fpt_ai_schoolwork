class Stock():
    def __init__(self, symbol, start, end):
        self.__symbol = symbol
        self.__prices = [(start, end)]
    def getSymbol(self):
        return self.__symbol
    def getPrices(self):
        return self.__prices
    def addPrices(self, start, end):
        self.__prices.append((start, end))
    def displayInfo(self):
        for i in range(len(self.__prices)):
            print(f"\nStock recorded on day {i+1}")
            print(f"Stock symbol: {self.getSymbol()}")
            print("Started out at: {:.3f}".format(self.getPrices()[i][0]))
            print("Ended at {:.3f}".format(self.getPrices()[i][1]))
        

class StockMarket():
    seen = set()
    stockList = list()
    def mainMenu(self):
        while True:
            print("\nMAIN MENU:")
            print("1. READ FILE")
            print("2. SEARCH BY STOCK SYMBOL")
            print("3. SEARCH BY INCREASING TREND")
            print("4. SEARCH BY BIGGEST DAILY INCREASE")
            print("5. EXIT")

            choice = input("Enter your choice: ")

            if choice == '1':
                fhand = input("Enter file name: ")
                self.readFile(fhand)
                self.displayStocksAvg()
            elif choice == '2':
                self.searchStockMaxMin()
            elif choice == '3':
                self.searchStockIncreasingDay1_2()
            elif choice == '4':
                maxDay = int(input("Enter the number of days: "))
                self.searchMaxNoOfIncreasingDay(maxDay)
            elif choice == '5':
                print("Author: Cao Tran Vuong")
                print("Student ID: HE191055")
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        
    def readFile(self, fhand):
        with open(fhand, 'r') as file:
            n = file.readline()
            lines = list(file.readlines())
            for line in lines:
                dataList = line.strip().split(' ')
                symbol = dataList[0]
                start = float(dataList[1])
                end = float(dataList[2])
                if symbol not in self.seen:
                    self.seen.add(symbol)
                    stock = Stock(symbol, start, end)
                    self.stockList.append(stock)
                else:
                    for stock in self.stockList:
                        if stock.getSymbol() == symbol:
                            stock.addPrices(start, end)
    
    def displayStocksAvg(self):
        sortedStockList = sorted(self.stockList, key = lambda x: x.getSymbol())
        for stock in sortedStockList:
            sumStart = 0
            sumEnd = 0
            print(f"\n{stock.getSymbol()}")
            cnt = 1
            for start, end in stock.getPrices():
                print(f"Day {cnt}: ")
                print(f"Started at {start}")
                print(f"Ended at {end}")
                sumStart += start
                sumEnd += end
                cnt += 1
                if cnt > 10:
                    break
            print("Average differential over a {} days period: {:.3f}".format(cnt-1, (sumEnd - sumStart)/(cnt-1)))

    def searchStockMaxMin(self):
        symbol = input("Enter stock symbol: ")
        for stock in self.stockList:
            if stock.getSymbol() == symbol:
                print("\nStock found")
                print(f"{symbol}")
                prices = stock.getPrices()
                high = max(prices[-10:], key = lambda x: x[1])
                low = min(prices[-10:], key = lambda x: x[1])
                print(f"Highest closing price: {high[1]}")
                print(f"Lowest closing price: {low[1]}")
                return 1
        print("\nStock not found")

    def searchStockIncreasingDay1_2(self):
        for stock in self.stockList:
            prices = stock.getPrices()
            if prices[0][0] >= prices[0][1] or prices[1][0] >= prices[1][1]:
                continue
            print(stock.getSymbol())

    def searchMaxNoOfIncreasingDay(self, maxDay):
        cnt = dict()
        maxCount = 0
        for stock in self.stockList:
            prices = stock.getPrices()
            dayCount = 1
            count = 0
            for start, end in prices:
                dayCount += 1
                if end > start:
                    count += 1
                if dayCount > maxDay:
                    break
            cnt[stock.getSymbol()] = count
            if maxCount < count:
                maxCount = count

        for symbol in cnt:
            if cnt[symbol] == maxCount:
                print(f"{symbol}: {maxCount} increasing days")

stockMarket = StockMarket()
stockMarket.mainMenu()
