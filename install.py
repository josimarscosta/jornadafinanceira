#!/usr/bin/env python3
"""
Script de instalação automática para Jornada Interativa - Fundamentos Financeiros
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Executa um comando e exibe o progresso"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} concluído!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro em {description}: {e}")
        print(f"Saída do erro: {e.stderr}")
        return False

def check_python_version():
    """Verifica se a versão do Python é compatível"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 ou superior é necessário!")
        print(f"Versão atual: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detectado")
    return True

def main():
    """Função principal de instalação"""
    print("🚀 Instalador da Jornada Interativa - Fundamentos Financeiros")
    print("=" * 60)
    
    # Verificar versão do Python
    if not check_python_version():
        return False
    
    # Verificar se pip está disponível
    if not run_command("pip --version", "Verificando pip"):
        print("💡 Tentando instalar pip...")
        if not run_command("python -m ensurepip --upgrade", "Instalando pip"):
            return False
    
    # Atualizar pip
    run_command("pip install --upgrade pip", "Atualizando pip")
    
    # Instalar dependências
    if not run_command("pip install -r requirements.txt", "Instalando dependências"):
        return False
    
    print("\n🎉 Instalação concluída com sucesso!")
    print("\n📋 Para executar o aplicativo:")
    print("   streamlit run app.py")
    print("\n🌐 O aplicativo será aberto automaticamente no navegador")
    print("   URL: http://localhost:8501")
    
    # Perguntar se deseja executar agora
    try:
        resposta = input("\n❓ Deseja executar o aplicativo agora? (s/n): ").lower().strip()
        if resposta in ['s', 'sim', 'y', 'yes']:
            print("\n🚀 Iniciando aplicativo...")
            os.system("streamlit run app.py")
    except KeyboardInterrupt:
        print("\n👋 Instalação finalizada. Execute 'streamlit run app.py' quando quiser usar o aplicativo.")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        print("\n❌ Instalação falhou. Verifique os erros acima e tente novamente.")
        sys.exit(1)

