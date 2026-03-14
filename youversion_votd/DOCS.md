# YouVersion Versículo do Dia

Exibe o Versículo do Dia da [YouVersion Bible API](https://developers.youversion.com) como sensor no Home Assistant.

## Configuração

| Opção               | Descrição                                                      | Padrão |
|---------------------|----------------------------------------------------------------|--------|
| `app_key`           | **Obrigatório.** Sua App Key da YouVersion Platform            | —      |
| `bible_version_id`  | ID numérico da versão da Bíblia                                | `1588` |
| `update_hour`       | Hora do dia (0–23) em que o versículo é atualizado             | `0`    |

### Como obter sua App Key

1. Acesse [platform.youversion.com](https://platform.youversion.com)
2. Crie uma conta e registre seu app
3. Copie o **App Key** gerado e cole na configuração do addon

### Versões em Português disponíveis

| ID     | Versão |
|--------|--------|
| `1588` | NVI — Nova Versão Internacional |
| `128`  | NVT — Nova Versão Transformadora |
| `211`  | ARA — Almeida Revista e Atualizada |
| `59`   | ARC — Almeida Revista e Corrigida |

## Sensor criado

O addon cria automaticamente o sensor `sensor.youversion_versiculo_do_dia`.

**Atributos disponíveis:**

| Atributo        | Descrição                        |
|-----------------|----------------------------------|
| `text`          | Texto completo do versículo      |
| `reference`     | Referência (ex: `JHN 3 16`)      |
| `passage_id`    | ID USFM (ex: `JHN.3.16`)         |
| `bible_version` | ID da versão usada               |
| `copyright`     | Aviso de copyright da versão     |
| `updated_at`    | Timestamp da última atualização  |

## Card no Dashboard (Lovelace)

```yaml
type: markdown
title: "📖 Versículo do Dia"
content: >
  ### {{ state_attr('sensor.youversion_versiculo_do_dia', 'reference') }}

  *{{ state_attr('sensor.youversion_versiculo_do_dia', 'text') }}*

  `{{ state_attr('sensor.youversion_versiculo_do_dia', 'copyright') }}`
```
