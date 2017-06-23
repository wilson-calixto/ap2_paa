#include <bits/stdc++.h>
#define NULA 0
#define BRANCO 1
#define CINZA 2
#define PRETO 3

using namespace std;




class Tupla {
private:
	double peso;
	int indice;
	
public:
	void setPeso(double peso) {
		this->peso = peso;
	}
	
	void setIndice(int indice) {
		this->indice = indice;
	}
	
	double getPeso() {
		return peso;
	}
	
	int getIndice() {
		return indice;
	}
};

class Item {
private:
	int num;
	int cor;
	int d,f;
	int inimigo;
	Item *anterior;
	vector<Tupla> adj;
	int sInicial, sFinal;
public:
	Item() {
		this->d = 0;
		this->f = 0;
		this->num = 0;
		this->cor = NULA;
		this->anterior=NULL;
		this->inimigo = false;	
	}
	
	int getNum() {
		return num;
	}
	int getIndice() {
		return num;
	}
	void setNum(int num) {
		this->num = num;
	}
	void setCor(int cor) {
		this->cor = cor;
	}
	int getCor() {
		return this->cor;
	}
	
	double getPeso(int k) {
		return adj[k].getPeso();
	}
	
	void setDescoberta(int d) {
		this->d = d;
	}
	void incrementa() {
		++this->d;
	}
	void setFinal(int f) {
		this->f = f;
	}
	
	int getIndice(int k) {
		return adj[k].getIndice();
	}	
		
	vector<Tupla> getAdj() {
		return adj;
	}
	
	void setAdj(Tupla n) {
		adj.push_back(n);
	}
	
	void setAnterior(Item *item) {
		this->anterior = item;
	}
	
	int size() {
		return adj.size();
	}

	void setInimigo() {
		this->inimigo = true;
	}

	void ordenaAdj(){
		shellsort(adj);
	}
	void shellsort(vector<Tupla> &v){
			 int h = 1;
			 while(h < v.size()/3){
			      h = 3*h+1;
			 }
			 
			 while(h >= 1){
			      for(int i = h; i < v.size(); i++){
				   int j = i;
				   while(j >= h && v[j].getIndice() < v[j-h].getIndice()){
				        swap(v[j], v[j-h]);
				        j = j-h;
				   }
			      }
			      h = h/3;
			 }
		}

};

class SubGrafo
{
public:
//private:
	vector<Item> vertices;
	vector<int> adj;
	int ord, m, indice, cor; 
	double distancia;
	bool inimigo;
	SubGrafo *anterior;
//public:
	SubGrafo(int a,int b) {
		inimigo = false;
	}
	SubGrafo() {
		inimigo = false;
	}
	void insertEdge(int u, int v, double peso) {
		Tupla t;
		t.setIndice(v);
		t.setPeso(peso);
		vertices[u].setAdj(t);
		vertices[u].setNum(u);

		t.setIndice(u);
		vertices[v].setAdj(t);
		vertices[v].setNum(v);
	}
	
	void setAnterior(SubGrafo *anterior) {
		this->anterior = anterior;
	}
	
	SubGrafo* getAnterior() {
		return anterior;
	}
	
	void setCor(int cor) {
		this->cor = cor;
	}
	
	int getCor() {
		return cor;
	}
	
	void setAdj(int v) {
		adj.push_back(v);
	}
	
	int getAdj(int v) {
		return adj[v];
	}
	
	void setIndice(int indice) {
		this->indice = indice;
	}
	
	int getIndice() {
		return indice;
	}
	double getDistancia(){
		return distancia; 
	}
	void anda() {
		for (int k = 1; k <= ord; k++) {
			vertices[k].ordenaAdj();		
		}

		for (int k = 1; k <= ord; k++) {
			vertices[k].setCor(BRANCO);		
		}
		for (int k = 1; k <= ord; k++) {
			if(vertices[k].getCor()==BRANCO){
				anda_aux(vertices[k]);
			}
		}
		
		
	}

	void anda_aux(Item &item) {
		item.setCor(CINZA);
		vector<Tupla> adj1=item.getAdj();
		for(int i = 0; i < adj1.size();i++) {		
			if(vertices[adj1[i].getIndice()].getCor() == BRANCO) {
				distancia += adj1[i].getPeso();
				anda_aux(vertices[item.getIndice(i)]);


			}
		}
		item.setCor(PRETO);
	}
	
	void entrada(int ord, int m) {
		this->ord = ord;
		this->m = m;
		int a, b;
		double c;
	
		vector<Item> x(ord+1);
		vertices = x;
		for(int i = 1; i <= m; i++) {
			cin >> a >> b >> c;
			insertEdge(a, b, c);
		}
	}
	
	void setInimigo(bool valor) {
		inimigo = valor;
	}
	
	bool getInimigo() {
			return 	inimigo;
	}
	
	int size() {
		return adj.size();
	}
	void ordena_subgrafo(){	
	}
	
	

};

class Grafo
{
private:
	int ord, m;
	int sInicial, sFinal;
	vector<SubGrafo> vertices;
	
public:

	Grafo(int ord, int m) { 
		this->ord = ord;
		this->m = m;
		vector<SubGrafo> x(ord+1);
		vertices = x;
		
		for(int i = 1; i <= ord; i++) vertices[i].setInimigo(false);
	}
	
	double menorCaminho() {
		
		return menorCaminho(sInicial, sFinal);
	}
	
	double menorCaminho(int origem, int destino) {

		double distancia = 0.0;
		BFS(origem);
	
		SubGrafo *aux;
		aux = &vertices[destino];
		
		while(aux != NULL) {

		
			aux->anda();
			distancia +=aux->getDistancia();
			aux = aux->getAnterior();
		}
		return distancia;			
	}
	
	int getTamanho() {
		return m;
	}
	
	void setIncial(int sInicial){
		this->sInicial=sInicial;
	}
	void setFinal(int sFinal){
		this->sFinal=sFinal;
	}
	
	void setOrdem(int ordem){
		this->ord=ordem;
	}
	
	void setTamanho(int tamanho) {
		this->m=tamanho;	
	}
	
	SubGrafo getVertice(int num) {
		return vertices[num];
	}

	void insertEdge(int u, int v) {
		vertices[u].setAdj(v);
		vertices[u].setIndice(u);
		vertices[v].setAdj(u);
		vertices[v].setIndice(v);
	}
	
	void entradaSubGrafo() {
		int ordem, tamanho;
		for(int i = 1; i <= ord; i++) {
			cin >> ordem >> tamanho;
			vertices[i].entrada(ordem, tamanho);
		}
	}
		
	
	void BFS(int origem) {
		BFS(vertices[origem]);
	}

	void BFS(SubGrafo &s) {

		for (int k = 1; k <= ord; k++) {			
		
			if(s.getIndice() == k) vertices[k].setCor(CINZA);
			else vertices[k].setCor(BRANCO);

			vertices[k].setAnterior(NULL);				
		}

		list<SubGrafo> fila;
		fila.push_back(s);
		vertices[0].setCor(PRETO);
		while(!fila.empty()) {
		
			SubGrafo u = fila.front();
			fila.pop_front();
			
			
			for(int i = 0; i < u.size(); ++i) {
				if(vertices[u.getAdj(i)].getCor() == BRANCO && (!getInimigo(u.getAdj(i)))) {
				
					vertices[u.getAdj(i)].setCor(CINZA);
					vertices[u.getAdj(i)].setAnterior(&vertices[u.getIndice()]);
					fila.push_back(vertices[u.getAdj(i)]);
				}
			}
			vertices[u.getIndice()].setCor(PRETO);
		}
	}
	void setInimigo(int indice) {
		vertices[indice].setInimigo(true);
	}
	
	bool getInimigo(int indice) {
			return 	vertices[indice].getInimigo();
	}

};


void entradaSuperGrafo(Grafo &supergrafo) {
	
		int a, b;
				
		for(int i = 1; i <= supergrafo.getTamanho(); i++) {
			cin >> a; 
			cin >> b;
			supergrafo.insertEdge(a, b);

		}
		
		int inimigos, sInicial, sFinal, num;
		cin >> inimigos;

		for(int i = 0; i < inimigos; i++) {
			cin >> num;
			supergrafo.setInimigo(num);
		}
		
		cin >> sInicial >> sFinal;			
		supergrafo.setIncial(sInicial);
		supergrafo.setFinal(sFinal);
		supergrafo.entradaSubGrafo();	
		cout << fixed << supergrafo.menorCaminho() << endl;
			
}

int main(int argc, const char * argv[])
{

	cout.precision(1);
	int ordem, tamanho;
	cin >> ordem >> tamanho;
	Grafo supergrafo(ordem, tamanho);
	entradaSuperGrafo(supergrafo);	
	return 0;
}
